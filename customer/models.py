from django.db import models
from accounts.models import CustUser
from store.models import Product


class Cart(models.Model):
    status=models.CharField(max_length=100,default="carted")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="c_product")
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="cart_user")
    
    
    
class Payment(models.Model):
    bank=models.CharField(max_length=200)
    acholdername=models.CharField(max_length=100)
    accno=models.IntegerField()
    ifsc=models.CharField(max_length=100,)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="u_payment")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="p_payment")
    quantity=models.PositiveIntegerField()
    status=models.CharField(max_length=100)
        
        