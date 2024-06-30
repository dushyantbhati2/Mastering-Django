from django.contrib.messages import constants as default_constants

CRITICAL = 50

DEFAULT_TAGS = {
    default_constants.DEBUG: 'debug',
    default_constants.INFO: 'info',
    default_constants.SUCCESS: 'success',
    default_constants.WARNING: 'warning',
    default_constants.ERROR: 'error',
    CRITICAL: 'critical',
}