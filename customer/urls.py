from django.urls import path
from .views import *


urlpatterns = [
    path('home/',MainHome.as_view(),name="uh"),
    path('product/',ProductView.as_view(),name="pv"),
    path('addtocart/<int:cid>/',addtocart,name="ac"),
    path('addtocartbuy/<int:cid>/',buycart,name="bc"),
    path('cart/',CartView.as_view(),name="cart"),
    path('removec/<int:pk>/',RemoveCart.as_view(),name="rc"),
    path('buy/<int:pid>/',BuyView.as_view(),name="buy"),
    path('confirmpay/<int:pid>/',PaymentConfirm,name="pay"),
    path('mc/',MyOrders.as_view(),name="mc"),

]
