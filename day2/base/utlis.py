from django.contrib.messages import add_message
from . import constants

def critcal(request,message,extra_tags="",fail_silently=False):
    add_message(
        request,
        constants.CRITICAL,
        message,
        extra_tags=extra_tags,
        fail_silently=fail_silently
    )