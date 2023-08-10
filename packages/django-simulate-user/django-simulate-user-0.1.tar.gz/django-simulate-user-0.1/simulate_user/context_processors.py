from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from django.utils import timezone
from .app_settings import app_settings
from .forms import UserSwitchForm
from .models import SimulatedUserSession


UserModel = get_user_model()


# noinspection PyProtectedMember
def simulate_user_context(request):
    """
    Context Processor: simulate_user_context

    Provides context variables related to the user simulation feature in the app.

    Parameters:
    - request (HttpRequest): The current HttpRequest object.

    Returns:
    - dict: A dictionary containing the necessary context variables.

    Context Variables:
    - simulate_user_form (UserSwitchForm): The form used to switch or simulate different users.
    - switch_simulated_user_url (str): The URL endpoint for switching simulated users.
    - show_simulated_user_control_bar (bool): Indicates if the simulation control bar should be shown.
    - simulated_user_control_bar_enabled (bool): Indicates if the control bar is active/enabled.
    - time_since_last_change: Indicates the time passed since the last simulation change.

    Functionality:
    - Determines the current state of the user, whether they are in a simulation or not.
    - Checks conditions and settings to decide the visibility and activity state of the simulation control bar.
    - Sets the initial data for the UserSwitchForm based on the current simulation state.

    Usage:
    This context processor should be added to the 'context_processors' option in Django's template settings to
    ensure that the required context variables are available in every template.
    """
    control_condition = getattr(request.real_user, app_settings.SIMULATED_USER_CONTROL_CONDITION, False)
    primary_key_name = UserModel._meta.pk.name
    if isinstance(request.user, AnonymousUser):
        simulated_user_pk = 'unauthenticated'
    elif request.user != request.real_user:
        simulated_user_pk = getattr(request.user, primary_key_name)
    else:
        simulated_user_pk = None
    if control_condition:
        records = SimulatedUserSession.objects.filter(real_session_key=request.session.session_key)
        results_1 = records.filter(hide_bar=True).exists()

        records = SimulatedUserSession.objects.filter(simulated_session_key=request.session.session_key)
        results_2 = records.filter(hide_bar=True).exists()
        hide_bar = results_1 or results_2
    else:
        hide_bar = True
    try:
        simulated_session = SimulatedUserSession.objects.get(simulated_session_key=request.session.session_key)
        time_since_last_change = timezone.now() - simulated_session.created_at
    except SimulatedUserSession.DoesNotExist:
        time_since_last_change = "Not in a simulation"

    form_initial_data = {
        'user_pk': simulated_user_pk if simulated_user_pk != 'unauthenticated' else None,
        'username': '',
        'email': '',
        'unauthenticated': simulated_user_pk == 'unauthenticated',
        'enabled': simulated_user_pk is not None,
        'hide': hide_bar
    }
    form = UserSwitchForm(initial=form_initial_data)

    if control_condition:
        show_bar = not hide_bar
    else:
        show_bar = False

    if not show_bar:
        bar_enabled = False
    else:
        bar_enabled = simulated_user_pk is not None

    if not app_settings.ONLY_ALLOW_SIMULATED_GET_REQUESTS:
        bar_enabled = False

    context = {
        'simulate_user_form': form,
        'switch_simulated_user_url': reverse('simulate_user_switch_user'),
        'show_simulated_user_control_bar': show_bar,
        'simulated_user_control_bar_enabled': bar_enabled,
        'time_since_last_change': time_since_last_change
    }

    return context
