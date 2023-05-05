from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import RegForm
from .forms import LogForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustUser



# Create your views here.

    
    
class RegView(CreateView) :
    template_name="reg.html"
    form_class=RegForm
    model=CustUser
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Registration Successful!!!") 
        return super().form_valid(form) 
    success_url=reverse_lazy("log") 
    
        
 
    
class LogView(FormView):
 template_name="login.html"
 form_class=LogForm
 def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                  login(request,user)
                  if request.user.usertype =="Store":
                      return redirect("sh")
                  else:
                      return redirect("uh")
            else:
              return render(request,"login.html",{"form":form_data})
        else:
            return render(request,"login.html",{"form":form_data})              
           
class LogOut(View) :
    def get(self,request):
        logout=(request)
        return redirect("log")     
    

    

             
           