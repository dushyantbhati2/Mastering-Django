from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . import models # Ensure you import utils, not utlis
from .utlis import decrypt_data
from cryptography.fernet import Fernet

# Create your views here.
def test(request):
        details = models.BankDetails.objects.get(user=request.user)
        
        acc_no=decrypt_data(details.accno)
        
        return JsonResponse({'account_number': acc_no}, safe=False)