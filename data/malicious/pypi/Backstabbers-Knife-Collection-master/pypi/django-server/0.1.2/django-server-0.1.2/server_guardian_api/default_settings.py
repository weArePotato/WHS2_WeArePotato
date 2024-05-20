"""Default settings for the ``server_guardian_api`` app."""
from django.conf import settings

PROCESSORS = getattr(
    settings,
    'SERVER_GUARDIAN_PROCESSORS',
    ['server_guardian_api.processors.debug.dummy_processor']
)

SECURITY_TOKEN = settings.SERVER_GUARDIAN_SECURITY_TOKEN
