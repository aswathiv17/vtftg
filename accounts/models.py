from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustUser(AbstractUser):
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    options=(
        ("Store","Store"),
        ("Customer","Customer")
    )
    usertype=models.CharField(max_length=100,choices=options,default="CustomerUser")
    
    options=(
        ("male","male"),
        ("female","female"),
        ("others","others")
    )
    gender=models.TextField(max_length=100,choices=options,default="gender")
    
    

    