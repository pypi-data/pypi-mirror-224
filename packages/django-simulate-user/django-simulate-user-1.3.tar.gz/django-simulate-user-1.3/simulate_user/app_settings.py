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
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class SimulateUserSettings:
    """
    Handles default settings and project overridden settings for the simulateuser app.
    """

    # Define default settings
    defaults: dict[str, any] = {
        'SIMULATED_USER_CONTROL_CONDITION': 'is_staff',
        'PRIVATE_CONTENT_REPLACEMENT': 'HIDDEN FOR USER PRIVACY PURPOSES',
        'SIMULATED_SESSION_EXPIRY': 3600,
        'SIMULATED_SESSION_RETENTION': 14,
        'ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS': True,
        'ENABLE_SIMULATE_USER': True,
        'ENABLE_SIMULATE_USER_NOTIFICATIONS': True,
        'SIMULATE_USER_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.ModelBackend',
        'SIMULATE_USER_PERMISSIONS': [
            {"SIMULATED_USER_ATTRIBUTE": "is_active", "REAL_USER_ATTRIBUTE": "is_staff"}
        ]
    }

    expected_types: dict[str, any] = {
        'SIMULATED_USER_CONTROL_CONDITION': str,
        'PRIVATE_CONTENT_REPLACEMENT': str,
        'SIMULATED_SESSION_EXPIRY': int,
        'SIMULATED_SESSION_RETENTION': int,
        'ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS': bool,
        'ENABLE_SIMULATE_USER': bool,
        'ENABLE_SIMULATE_USER_NOTIFICATIONS': bool,
        'SIMULATE_USER_AUTHENTICATION_BACKEND': str,
        'SIMULATE_USER_PERMISSIONS': list
    }

    def __getattr__(self, name: str) -> any:
        value = getattr(settings, name, self.defaults.get(name))
        expected_type = self.expected_types.get(name)

        if expected_type and not isinstance(value, expected_type):
            raise TypeError(f"Expected type for {name} is {expected_type}, but got {type(value)}.")

        if name == 'SIMULATED_USER_CONTROL_CONDITION':
            self.validate_user_control_condition(value)

        if name == 'SIMULATE_USER_PERMISSIONS':
            self.validate_user_permissions(value)

        return value

    @staticmethod
    def validate_user_control_condition(condition: str) -> None:
        """Validates if the given condition corresponds to a boolean attribute of the User model."""
        if not hasattr(UserModel, condition):
            raise ValueError(f"'{condition}' is not an attribute of the User model.")

        attribute_type = type(getattr(UserModel, condition))
        if attribute_type != bool:
            raise ValueError(f"'{condition}' is not a boolean attribute of the User model.")

    def validate_user_permissions(self, permissions: list) -> None:
        """Validates the SIMULATE_USER_PERMISSIONS setting."""
        if not all(isinstance(perm, dict) for perm in permissions):
            raise TypeError("All elements in 'SIMULATE_USER_PERMISSIONS' should be dictionaries.")

        for perm in permissions:
            for key in ['SIMULATED_USER_ATTRIBUTE', 'REAL_USER_ATTRIBUTE']:
                if key not in perm:
                    raise TypeError(
                        f"Each dictionary in 'SIMULATE_USER_PERMISSIONS' must contain the key '{key}'.")

                self.validate_user_control_condition(perm[key])


# Create an instance of the class, so we can use its attributes
app_settings: SimulateUserSettings = SimulateUserSettings()
