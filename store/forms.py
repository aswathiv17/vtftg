from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=["user"]
        widgets={
            "productname":forms.TextInput(attrs={"class":"forms-control","placeholder":"productname"}),
            "image":forms.FileInput(),
            "price":forms.NumberInput(attrs={"class":"forms-control","placeholder":"price"}),
            "ram":forms.TextInput(attrs={"class":"forms-control","placeholder":"ram"}),
            "rom":forms.TextInput(attrs={"class":"forms-control","placeholder":"rom"}),
            "battery":forms.TextInput(attrs={"class":"forms-control","placeholder":"battery"}),
            "processor":forms.TextInput(attrs={"class":"forms-control","placeholder":"proccesor"}),
        }
class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=50,label="current password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    new_password=forms.CharField(max_length=50,label="new password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    confirm_password=forms.CharField(max_length=50,label="confirm password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
        
      
        
        