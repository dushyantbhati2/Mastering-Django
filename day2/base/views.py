from django.shortcuts import render,HttpResponse
from django.contrib import messages
from base import critcal
# Create your views here.

def index(request):
    messages.success(request, 'Your action was successful!')
    
    # Add an error message
    messages.error(request, 'There was an error with your action.')

    # Add a warning message
    messages.warning(request, 'This is a warning message.')

    # Add an info message
    messages.info(request, 'This is an informational message.')

    # Add a debug message
    messages.debug(request, 'This is a debug message.')
    
    critcal(request,"this is a critical message")

    return render(request,"index.html")