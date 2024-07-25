from django.db import models
from django.contrib.auth.models import User
from .utlis import encrypt_data
# Create your models here. 
class BankDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    accno=models.CharField(max_length=100)

    def save(self,*args, **kwargs):
        self.accno=encrypt_data(data=self.accno)
        return super().save(*args,**kwargs)
    
    