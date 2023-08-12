from django.conf import settings
from django.core.checks import Warning, register, Tags
from .app_settings import app_settings


@register(Tags.compatibility)
def check_settings_combination(app_configs, **kwargs):
    warnings = []

    if app_settings.ENABLE_MIMICRY and not settings.DEBUG:
        warnings.append(
            Warning(
                "'ENABLE_MIMICRY' being true at the same time as you are in production is very inefficient and "
                "not very very secure.",
                hint="Review your settings and adjust as needed.",
                id="mimicry.W001",
            )
        )

    return warnings
