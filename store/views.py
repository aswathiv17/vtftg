from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.models import CustUser
from django.urls import reverse_lazy

from .forms import *
from .models import *



# Create your views here.
class StoreHome(TemplateView):
    template_name="storehome.html"

# Create your views here.



class AddProductView(CreateView):
    template_name="addproduct.html"
    form_class=ProductForm
    model=Product
    success_url=reverse_lazy('sh')
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,'product added')
        return super().form_valid(form)
    
    
class MyProduct(TemplateView): 
    template_name="myproduct.html"    
    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)  
        context["data"]=Product.objects.filter(user=self.request.user) 
        return context    
    
    
             
class DeleteProduct(DeleteView):
    model=Product
    template_name="deleteproduct.html"
    success_url=reverse_lazy("mp")
    pk_url_kwargs="pk"
    
    
class EditProductView(UpdateView):
    form_class=ProductForm
    model=Product
    template_name="editproduct.html"
    success_url=reverse_lazy("mp")
    pk_url_kwargs="pk"
           
class ChangePassword(FormView):
    template_name="ChangePassword.html"
    form_class=ChangePasswordForm
    def post(self,request,*args, **kwargs):
        form_data=ChangePasswordForm(data=request.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("current_password")
            new=form_data.cleaned_data.get("new_password")
            confirm=form_data.cleaned_data.get("confirm_password")
            print(current)
            user=authenticate(request,username=request.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(request,"password changed")
                    logout(request)
                    return redirect("log")
                else:
                    messages.error(request,"passwords mismatches")
                    return redirect("cp")
            else:
                    messages.error(request,"passwords INCORRECT")
                    return redirect("cp")
        else:
            return render(request,"changepassword.html",{"form":form_data})
           
           
           
             
                 
    
    

