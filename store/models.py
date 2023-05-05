from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *


# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="product_image")
    price=models.IntegerField()
    ram=models.CharField(max_length=100)
    rom=models.CharField(max_length=100)
    battery=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="p_user")
    
    
        
     
    


# Create your models here.
