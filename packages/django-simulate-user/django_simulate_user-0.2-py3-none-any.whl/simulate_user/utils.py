from functools import wraps
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from django.utils import timezone
from .app_settings import app_settings
from .models import SimulatedUserSession, SimulatedUserAction


UserModel = get_user_model()


def reset_real_user(view_func=None, *, request=None):
    """
    Decorator function to reset the 'real_user' attribute on the request object.
    If used without arguments, it will also reset 'simulated_user_pk' if it exists.

    Args:
    - view_func: View function to be wrapped.
    - request: The request object.

    Returns:
    - Function: The wrapped function or the decorator itself.
    """
    # noinspection PyShadowingNames
    def decorator(view_func):
        # noinspection PyShadowingNames
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            request.real_user = request.user
            if getattr(request,  'simulated_user_pk', None):
                request.simulated_user_pk = None
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    if view_func is not None:
        return decorator(view_func)

    if request is not None:
        request.real_user = request.user
        if getattr(request, 'simulated_user_pk', None):
            request.simulated_user_pk = None


# noinspection PyProtectedMember
def new_simulated_session(request, hide_bar=False):
    """
    Create a new simulated session for the user.

    Args:
    - request: The request object.
    - hide_bar: Boolean indicating if the simulation bar should be hidden.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition = getattr(request.real_user, app_settings.SIMULATED_USER_CONTROL_CONDITION, False)
    request.simulated_user_pk = getattr(request, 'simulated_user_pk', None)
    if control_condition and request.simulated_user_pk:
        real_session_key = request.session.session_key
        if not (request.simulated_user_pk == 'unauthenticated' or request.simulated_user_pk is None):
            request.session['_auth_user_id'] = request.simulated_user_pk

        simulated_session = SimulatedUserSession()
        simulated_session.real_user = request.real_user
        if hide_bar:
            request = change_user(request, request.real_user)
            simulated_session.hide_bar = True
            simulated_session.closed_at = timezone.now()
        else:
            if request.simulated_user_pk == 'unauthenticated':
                request = change_user(request, AnonymousUser())
            else:
                try:
                    primary_key_field = UserModel._meta.pk.name
                    filter_kwargs = {primary_key_field: request.simulated_user_pk}
                    user_to_login = UserModel.objects.get(**filter_kwargs)
                    request = change_user(request, user_to_login)
                except UserModel.DoesNotExist:
                    request = change_user(request, AnonymousUser())
            if isinstance(request.user, AnonymousUser):
                simulated_session.simulated_user = None
            else:
                simulated_session.simulated_user = request.user
        simulated_session.real_session_key = real_session_key
        simulated_session.simulated_session_key = request.session.session_key
        try:
            simulated_session.save()
        except IntegrityError:
            pass
        request.session['_is_simulated_user_session'] = True

    return request


def set_hide_bar(request, hide_bar_status=True):
    """
    Sets the 'hide_bar' status for the current simulated session.

    Args:
    - request: The request object.
    - hide_bar_status: Boolean indicating the desired 'hide_bar' status.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition = getattr(request.real_user, app_settings.SIMULATED_USER_CONTROL_CONDITION, False)
    if control_condition:
        try:
            simulated_session = SimulatedUserSession.objects.get(
                simulated_session_key=request.session.session_key, closed_at__isnull=True
            )
            simulated_session.closed_at = timezone.now()
            simulated_session.hide_bar = hide_bar_status
            simulated_session.save()
        except SimulatedUserSession.DoesNotExist:
            request.simulated_user_pk = 'unauthenticated'
            request = new_simulated_session(request, hide_bar=True)
    return request


def disable_bar(request):
    """
    Disables the simulation bar and ends the current simulated session.

    Args:
    - request: The request object.

    Returns:
    - HttpRequest: Modified request object.
    """
    control_condition = getattr(request.real_user, app_settings.SIMULATED_USER_CONTROL_CONDITION, False)
    if control_condition:
        try:
            simulated_session = SimulatedUserSession.objects.get(
                simulated_session_key=request.session.session_key, closed_at__isnull=True
            )
            simulated_session.closed_at = timezone.now()
            simulated_session.save()
            request.real_user = simulated_session.real_user
            request = change_user(request, request.real_user)
            request.simulation_created_at = None
        except SimulatedUserSession.DoesNotExist:
            pass
    return request


def coordinate_request_with_simulated_session(request):
    """
    Coordinate the request with the currently active simulated session.

    Args:
    - request: The request object.

    Returns:
    - HttpRequest: Modified request object.
    """
    request.real_user = getattr(request, 'real_user', request.user)
    _is_simulated_user_session = getattr(request.session, '_is_simulated_user_session', False)
    if app_settings.ENABLE_SIMULATE_USER:
        session_key = request.session.session_key
        if _is_simulated_user_session:
            simulated_session = SimulatedUserSession.objects.filter(
                simulated_session_key=session_key
            ).first()
            if simulated_session and simulated_session.closed_at:
                request.real_user = simulated_session.real_user
                simulated_session = None

            if simulated_session:
                simulated_session.save()
                active_simulated_session = SimulatedUserSession.objects.filter(
                    simulated_session_key=session_key, closed_at__isnull=True
                ).first()
                if active_simulated_session and not simulated_session.hide_bar:
                    request.real_user = active_simulated_session.real_user
                    if active_simulated_session.simulated_user is None:
                        request = change_user(request, AnonymousUser())
                        log_simulated_action(
                            request,
                            active_simulated_session,
                            f"{request.real_user.username} simulating AnonymousUser accessed {request.path}"
                        )
                    else:
                        request = change_user(request, active_simulated_session.simulated_user)
                        log_simulated_action(
                            request,
                            active_simulated_session,
                            f"{request.real_user.username} simulating user: {request.user.username} accessed {request.path}"
                        )
                    request.simulation_created_at = active_simulated_session.created_at
                else:
                    request.real_user = simulated_session.real_user
                    request = change_user(request, request.real_user)
                    request.simulation_created_at = None
            else:
                request = change_user(request, request.real_user)
                request.simulation_created_at = None
        else:
            request = change_user(request, request.real_user)
            request.simulation_created_at = None
    else:
        request = change_user(request, request.real_user)
        request.simulation_created_at = None

    return request


def change_user(request, user):
    """
    Change the user of the current request.

    Args:
    - request: The request object.
    - user: The user object or AnonymousUser to be set on the request.

    Returns:
    - HttpRequest: Modified request object.
    """
    if request.user != user:
        real_user = getattr(request, 'real_user', request.user)
        simulation_created_at = getattr(request, 'simulation_created_at', None)
        simulated_user_pk = getattr(request, 'simulated_user_pk', None)
        if isinstance(user, UserModel):
            user.backend = app_settings.SIMULATE_USER_AUTHENTICATION_BACKEND
            login(request, user)
            request.session.save()
        else:
            request.session.clear()
            request.session.create()
            request.user = AnonymousUser()
        request.real_user = real_user
        request.simulation_created_at = simulation_created_at
        request.simulated_user_pk = simulated_user_pk

    return request


def log_simulated_action(request, simulated_session_instance, action_desc):
    """
    Log an action performed during a simulated session.

    Args:
    - request: The request object.
    - simulated_session_instance: Instance of the current simulated session.
    - action_desc: Description of the action performed.

    Returns:
    - None
    """
    if request.real_user != request.user:
        try:
            simulated_user_action = SimulatedUserAction.objects.create(
                simulated_user_session=simulated_session_instance,
                action=action_desc
            )
            simulated_user_action.save()
        except SimulatedUserSession.DoesNotExist:
            pass
