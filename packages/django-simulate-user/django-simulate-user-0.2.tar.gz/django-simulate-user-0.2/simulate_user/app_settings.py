"""
Settings Configuration for the simulate_user app.

This module provides default settings for the app and also retrieves overridden settings from the project's main `
settings.py` file if available.

Attributes:
- `SimulateUserSettings`: A class that handles fetching settings values.
- `app_settings`: An instance of the `SimulateUserSettings` class which is used to access the settings.

Default Settings:
- `SIMULATED_USER_CONTROL_CONDITION`: Default value is 'is_staff'. Determines the attribute or condition to control the
simulated user functionality.
- `PRIVATE_CONTENT_REPLACEMENT`: Default value is 'HIDDEN FOR USER PRIVACY PURPOSES'. The replacement content for
private or sensitive information during simulation.
- `SIMULATED_SESSION_EXPIRY`: Default value is 3600. The time (in seconds) for how long a simulated session lasts before
expiry.
- `SIMULATED_SESSION_RETENTION`: Default value is 14. The retention period (in days) for storing simulated session data.
- `ONLY_ALLOW_SIMULATED_GET_REQUESTS`: Default value is True. Restricts simulated user sessions to only allow GET
requests.
- `ENABLE_SIMULATE_USER`: Default value is True. Flag to enable or disable the entire simulate user functionality.
- `SIMULATE_USER_AUTHENTICATION_BACKEND`: Default value is 'django.contrib.auth.backends.ModelBackend'. The
authentication backend used for simulated users.

Usage:
Import the `app_settings` object and access the settings attributes as needed.
"""

from django.conf import settings


class SimulateUserSettings:
    """
    Handles default settings and project overridden settings for the simulateuser app.
    """
    def __getattr__(self, name):
        # Define default settings
        defaults = {
            'SIMULATED_USER_CONTROL_CONDITION': 'is_staff',
            'PRIVATE_CONTENT_REPLACEMENT': 'HIDDEN FOR USER PRIVACY PURPOSES',
            'SIMULATED_SESSION_EXPIRY': 3600,
            'SIMULATED_SESSION_RETENTION': 14,
            'ONLY_ALLOW_SIMULATED_GET_REQUESTS': True,
            'ENABLE_SIMULATE_USER': True,
            'SIMULATE_USER_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.ModelBackend'
        }

        # Check if the setting is overridden in the project's settings
        return getattr(settings, name, defaults.get(name))


# Create an instance of the class, so we can use its attributes
app_settings = SimulateUserSettings()
