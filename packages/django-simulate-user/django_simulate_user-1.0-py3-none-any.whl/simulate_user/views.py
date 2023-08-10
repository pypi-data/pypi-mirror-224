from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import UserSwitchForm
from .utils import new_simulated_session, disable_bar, set_hide_bar


UserModel = get_user_model()


# noinspection PyProtectedMember
def switch_user(request: HttpRequest) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
    """
    Switch the current user or simulate a user based on the form data submitted.

    This view supports:
    1. Hiding the simulation bar.
    2. Enabling/disabling user simulation.
    3. Simulating as an unauthenticated user.
    4. Switching to a user based on PK, username, or email.

    If the user is not found by PK, username, or email, the request is redirected to the previous page.
    If the simulation is disabled, the bar is hidden, and any simulated user state is reset.

    Args:
    - request: The request object.

    Returns:
    - HttpResponse: Redirects to the referring page or, if not available, the root URL.
    """
    if request.method == 'POST':
        form: UserSwitchForm = UserSwitchForm(request.POST)
        if form.is_valid():
            # Check if the "hide" checkbox is ticked.
            if form.cleaned_data.get('hide'):
                request: HttpRequest = set_hide_bar(request, True)

            # Check if the simulation is enabled.
            if form.cleaned_data.get('enabled'):
                user_pk: str | None = form.cleaned_data.get('user_pk')
                username: str | None = form.cleaned_data.get('username')
                email: str | None = form.cleaned_data.get('email')
                unauthenticated: bool = form.cleaned_data.get('unauthenticated')

                if unauthenticated:
                    request.simulated_user_pk = 'unauthenticated'
                    request: HttpRequest = new_simulated_session(request)
                elif user_pk:
                    primary_key_name: str = UserModel._meta.pk.name
                    try:
                        user: UserModel = UserModel.objects.get(**{primary_key_name: user_pk})
                        request.simulated_user_pk = getattr(user, primary_key_name)
                        request: HttpRequest = new_simulated_session(request)
                    except UserModel.DoesNotExist:
                        return redirect(request.META.get('HTTP_REFERER', '/'))
                elif username:
                    try:
                        user: UserModel = UserModel.objects.get(username=username)
                        request.simulated_user_pk = getattr(user, UserModel._meta.pk.name)
                        request: HttpRequest = new_simulated_session(request)
                    except UserModel.DoesNotExist:
                        return redirect(request.META.get('HTTP_REFERER', '/'))
                elif email:
                    try:
                        user: UserModel = UserModel.objects.get(email=email)
                        request.simulated_user_pk = getattr(user, UserModel._meta.pk.name)
                        request: HttpRequest = new_simulated_session(request)
                    except UserModel.DoesNotExist:
                        return redirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                # Disable the simulation bar and reset the simulated user state.
                request: HttpRequest = disable_bar(request)
                if getattr(request, 'simulated_user_pk', None):
                    request.simulated_user_pk = None

    # Redirect to the referring page or the root URL if the referrer is not available.
    return redirect(request.META.get('HTTP_REFERER', '/'))
