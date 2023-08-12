from django.conf import settings
from django.core.checks import Warning, register, Tags
from simulate_user.app_settings import app_settings


@register(Tags.compatibility)
def check_settings_combination(app_configs, **kwargs):
    warnings = []

    if app_settings.ENABLE_SIMULATE_USER and not settings.DEBUG:
        warnings.append(
            Warning(
                "'ENABLE_SIMULATE_USER' being true at the same time as you are in production is very inefficient and "
                "not very very secure.",
                hint="Review your settings and adjust as needed.",
                id="simulate_user.W001",
            )
        )

    return warnings
