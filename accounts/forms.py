from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=['first_name','last_name','email','gender','phone','address','usertype','username','password1','password2']
        widgets={
            "gender":forms.RadioSelect()
        }
        
        
class LogForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))    
    
    

            