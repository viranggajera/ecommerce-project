

"""
URL configuration for ecommerce project.

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
from django.contrib import admin
from django.urls import path,include
from app_seller import views
urlpatterns = [
    path('seller_index/', views.seller_index, name="seller_index"),
    path("seller_about/", views.seller_about,name="seller_about"),
    path("seller_signup/",views.seller_signup, name="seller_signup"),
    path("seller_login/", views.seller_login,name="seller_login"),
    path("seller_otp/",views.seller_otp, name="seller_otp"),
    path("seller_add_product/",views.seller_add_product,name="seller_add_product"),
    path("seller_logout/", views.seller_logout, name="seller_logout"),
    path("seller_profile/",views.seller_profile,name="seller_profile"),
    path("selelr_contact/", views.seller_contact, name="seller_contact"),
    path("seller/", views.seller, name="seller"),
    path('buyer',views.buyer, name="buyer"),
    
    
    
]