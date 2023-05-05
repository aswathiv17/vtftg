from django.urls import path
from .views import *


urlpatterns = [
    path('store/',StoreHome.as_view(),name="sh"),
    path('addproduct/',AddProductView.as_view(),name="pro"),
    path('myproduct/',MyProduct.as_view(),name="mp"),
    path('delete/<int:pk>/',DeleteProduct.as_view(),name="dp"),
    path('edit/<int:pk>/',EditProductView.as_view(),name="ep"),
    path('cp/',ChangePassword.as_view(),name="cp"),

]
