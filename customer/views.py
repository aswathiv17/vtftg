from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *
from store.views import *





# Create your views here.
class MainHome(TemplateView):
    template_name="mainhome.html"
    
class ProductView(TemplateView): 
    template_name="productview.html"    
    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)  
        context["data"]=Product.objects.all() 
        return context    
    
    
def addtocart(request,*args,**kwargs):
        id=kwargs.get("cid")
        product=Product.objects.get(id=id)
        user=request.user
        Cart.objects.create(product=product,user=user,status="Carted")
        return redirect("uh")
    
def buycart(request,*args,**kwargs):
        id=kwargs.get("cid")
        product=Product.objects.get(id=id)
        user=request.user
        Cart.objects.create(product=product,user=user,status="Purchased")
        return redirect("uh")    
    
class CartView(TemplateView):
    template_name="addcart.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)  
        context["data"]=Cart.objects.filter(user=self.request.user,status= "Carted")
        
        return context
     
class RemoveCart(DeleteView):
    model=Cart
    template_name="removecart.html"
    success_url=reverse_lazy("uh")
    pk_url_kwargs="pk"
         
class BuyView(TemplateView):
    template_name="buy.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        id=kwargs.get("pid")
        context["data"]=Product.objects.filter(id=id)
        context["form"]=PaymentForm()
        return context
    
def PaymentConfirm(request,*args,**kwargs): 
     id=kwargs.get("pid") 
     product=Product.objects.get(id=id) 
     user=request.user 
     bank=request.POST.get('bank') 
     acholdername=request.POST.get('acholdername') 
     accno=request.POST.get('accno') 
     ifsc=request.POST.get('ifsc') 
     quantity=request.POST.get('quantity') 
     Payment.objects.create(bank=bank,acholdername=acholdername,accno=accno,ifsc=ifsc,quantity=quantity,product=product,user=user,status="Purchased") 
     return redirect("mc")    
         
class MyOrders(TemplateView):
    template_name="myorders.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Payment.objects.filter(user=self.request.user)
        return context


    
    
    
     
    
