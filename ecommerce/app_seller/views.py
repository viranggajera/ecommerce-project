

# Create your views here.
from django.shortcuts import render
from app_buyer.models import *
from app_seller.models import *
from django.conf import settings
from django.core.mail import send_mail





# Create your views here.
def seller_index(request):
    return render(request,"seller_index.html")

import random
def seller_signup(request):
    global name
    name="hello"
    context={}
    if request.method=="POST":
        try:
            user_exist=sellerUser.objects.get(email=request.POST["email"])
            context["msg"]="User Already Exist"
        except:

                global otp

                otp=random.randint(100000,999999)
                subject = 'OTP VERIFICATION PROCESS'
                message = f'Thanks for chosing us , your otp is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST["email"], ]
                send_mail( subject, message, email_from, recipient_list )
                global seller_data
                seller_data={
                    "username":request.POST["uname"],
                    "email":request.POST["email"],
                    "password":request.POST["password"],
                }
                return render(request,"seller_otp.html")
            
    return render(request,"seller_signup.html",context)

from django.contrib.auth.hashers import make_password,check_password

def seller_otp(request):
    context={}
    if request.method=="POST":
        if otp==int(request.POST["otp"]):
            sellerUser.objects.create(
                username=seller_data["username"],
                email=seller_data["email"],
                password=make_password(seller_data["password"]),
            )
            context["msg"]="Signup Succesfull"
            return render(request,"seller_signup.html",context)
        else:
            context["msg"]="Invalid OTP"
    return render(request,"seller_otp.html",context)


def seller_login(request):
    context={}
    if request.method=="POST":
        try:
            current_user=sellerUser.objects.get(email=request.POST["email"])
            print(current_user)
            
            if check_password(request.POST["password"], current_user.password):
                context["msg"]="LOGIN SUCCESFULL"
                request.session["email"]=request.POST["email"]
                seller_data=sellerUser.objects.get(email=request.session["email"])
                context["seller_data"]=seller_data
                return render(request,"seller_product.html",context)
            else:
                context["msg"]="Incorrect password"
        except:
            context["msg"]="Invalid User"
    return render(request,"seller_login.html",context)


def seller_logout(request):
    context={}
    del request.session["email"]
    context["msg"]="LOGOUT successfull"
    return render(request,"seller_login.html",context)

def seller_profile(request):
    context={}
    seller_data=sellerUser.objects.get(email=request.session["email"])
    context["seller_data"]=seller_data
    if request.method=="POST":
        seller_data.username=request.POST["uname"]
        seller_data.email=request.POST["email"]
        # password check
        if check_password(request.POST["opassword"],seller_data.password):
            if request.POST["npassword"]==request.POST["cnpassword"]:
                seller_data.password=make_password(request.POST["npassword"])
            else:
                context["seller_data"]="New Password nad confirm New password Not match"
        else:
            context["seller_data"]="Old Password Not match"
        
        request.FILES["propic"]
        seller_data.profile_pic= request.FILES["propic"]
        
        seller_data.save()
        context["msg"]="Profile Updated Successfully"
        context["seller_data"]=seller_data
    return render(request,"seller_profile.html",context)





def seller_product(request):
    context={}
    seller_data=sellerUser.objects.get(email=request.session["email"])
    context["seller_data"]=seller_data
    all_product=Product.objects.all()
    context["all_product"]=all_product
    return render(request,"seller_product.html",context)

def seller_about(request):
    return render(request,"seller_about.html")

def seller_contact(request):
    return render(request,"seller_contact.html")

 



def seller_add_product(request):
    context={}
    if request.method=="POST":
        user_exist=sellerUser.objects.get(email=request.session["email"])
        Product.objects.create(
            pname=request.POST["pname"],
            price=request.POST["price"],
            description=request.POST["des"],
            image=request.FILES["product_pic"],
            image1=request.FILES["product_pic1"],
            image2=request.FILES["product_pic2"],
            image3=request.FILES["product_pic3"],

            
            user=user_exist,
        )
        context["msg"]="product added succefully"
    return render(request,"seller_add_product.html",context)









def seller(request):
    return render(request,"seller.html")

def buyer(request):
    return render(request,"index.html")




