"""
Settings Configuration for the Mimicry app.

This module provides default settings for the app and also retrieves overridden settings from the project's main `
settings.py` file if available.

Attributes:
- `MimicrySettings`: A class that handles fetching settings values.
- `app_settings`: An instance of the `MimicrySettings` class which is used to access the settings.

Default Settings:
- `MIMICRY_FEATURE_CONTROL_CONDITION`: Default value is 'is_staff'. Determines the attribute or condition to control the
Mimicry functionality.
- `PRIVATE_CONTENT_REPLACEMENT`: Default value is 'HIDDEN FOR USER PRIVACY PURPOSES'. The replacement content for
private or sensitive information during simulation.
- `SIMULATED_SESSION_EXPIRY`: Default value is 3600. The time (in seconds) for how long a simulated session lasts before
expiry.
- `SIMULATED_SESSION_RETENTION`: Default value is 14. The retention period (in days) for storing simulated session data.
- `ONLY_ALLOW_SIMULATED_GET_REQUESTS`: Default value is True. Restricts simulated user sessions to only allow GET and
HEAD requests.
- `ENABLE_MIMICRY`: Default value is True. Flag to enable or disable the entire Mimicry functionality.
- `MIMICRY_AUTHENTICATION_BACKEND`: Default value is 'django.contrib.auth.backends.ModelBackend'. The
authentication backend used for simulated users.

Usage:
Import the `app_settings` object and access the settings attributes as needed.
"""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import BooleanField


UserModel = get_user_model()


class SimulateUserSettings:
    """
    Handles default settings and project overridden settings for the Mimicry app.
    """

    # Define default settings
    defaults: dict[str, any] = {
        'MIMICRY_FEATURE_CONTROL_CONDITION': 'is_staff',
        'PRIVATE_CONTENT_REPLACEMENT': 'HIDDEN FOR USER PRIVACY PURPOSES',
        'SIMULATED_SESSION_EXPIRY': 3600,
        'SIMULATED_SESSION_RETENTION': 14,
        'ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS': True,
        'ENABLE_MIMICRY': True,
        'ENABLE_SIMULATE_USER_NOTIFICATIONS': True,
        'MIMICRY_AUTHENTICATION_BACKEND': 'django.contrib.auth.backends.ModelBackend',
        'MIMICRY_PERMISSIONS': [
            {"SIMULATED_USER_ATTRIBUTE": "is_active", "REAL_USER_ATTRIBUTE": "is_staff"}
        ]
    }

    expected_types: dict[str, any] = {
        'MIMICRY_FEATURE_CONTROL_CONDITION': str,
        'PRIVATE_CONTENT_REPLACEMENT': str,
        'SIMULATED_SESSION_EXPIRY': int,
        'SIMULATED_SESSION_RETENTION': int,
        'ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS': bool,
        'ENABLE_MIMICRY': bool,
        'ENABLE_SIMULATE_USER_NOTIFICATIONS': bool,
        'MIMICRY_AUTHENTICATION_BACKEND': str,
        'MIMICRY_PERMISSIONS': list
    }

    def __getattr__(self, name: str) -> any:
        value = getattr(settings, name, self.defaults.get(name))
        expected_type = self.expected_types.get(name)

        if expected_type and not isinstance(value, expected_type):
            raise TypeError(f"Expected type for {name} is {expected_type}, but got {type(value)}.")

        if name == 'MIMICRY_FEATURE_CONTROL_CONDITION':
            self.validate_boolean_user_attribute(value)

        if name == 'MIMICRY_PERMISSIONS':
            self.validate_user_permissions(value)

        return value

    @classmethod
    def validate_boolean_user_attribute(cls, attr: str) -> None:
        """Validates if the given attribute corresponds to a boolean attribute of the User model."""
        field = cls.get_user_model_field(attr)
        if not isinstance(field, BooleanField):
            raise TypeError(f"'{attr}' is not a boolean field of the User model.")

    # noinspection PyProtectedMember
    @staticmethod
    def get_user_model_field(attr: str):
        """Retrieve field instance for a given attribute of the User model."""
        try:
            return UserModel._meta.get_field(attr)
        except Exception:
            raise TypeError(f"'{attr}' is not an attribute of the User model.")

    @classmethod
    def validate_user_permissions(cls, permissions: list) -> None:
        """Validates the SIMULATE_USER_PERMISSIONS setting."""
        if not all(isinstance(perm, dict) for perm in permissions):
            raise TypeError("All elements in 'MIMICRY_PERMISSIONS' should be dictionaries.")

        for perm in permissions:
            for key in ['SIMULATED_USER_ATTRIBUTE', 'REAL_USER_ATTRIBUTE']:
                if key not in perm:
                    raise TypeError(f"Each dictionary in 'MIMICRY_PERMISSIONS' must contain the key '{key}'.")
                cls.validate_boolean_user_attribute(perm[key])


# Create an instance of the class, so we can use its attributes
app_settings: SimulateUserSettings = SimulateUserSettings()
