"""
URL configuration for shopcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from app_buyer import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup,name="signup"),
    path('otp/', views.otp, name="otp"),
    path('login/',views.login, name="login"),
    path('Product/', views.product1, name="Product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact,name="contact"),
    path('logout/',views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('seller/', views.seller, name="seller"),
    path('buyer/', views.buyer, name="buyer"),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path("cart/<int:id>", views.cart, name="cart"),
    path("view_product/<int:id>", views.view_product,name="view_product"),
    path("view_cart/", views.cart_view, name="cart_view"),
    path("check_out/", views.check_out, name="check_out"),
    path("remove_cart/<int:id>", views.remove_cart, name="remove_cart"),
    path("update_cart/",views.update_cart, name="update_cart"),
    path("confirm_order/", views.confirm_order, name="confirm_order"),
    path("onlinepayment/", views.onlinepayment, name="onlinepayment"),
   path("product11/", views.product11, name="product11"),
   
    
    
    
  
   

   
    
    
]
