from django.shortcuts import render,redirect
from app_buyer.models import *
from app_seller.models import *
from django.conf import settings
from django.core.mail import send_mail





# Create your views here.
def index(request):
    return render(request,"index.html")

import random
def signup(request):
    
    context={}
    if request.method=="POST":
        try:
            user_exist=User.objects.get(email=request.POST["email"])
            context["msg"]="User Already Exist"
        except:

                global otp

                otp=random.randint(100000,999999)
                subject = 'OTP VERIFICATION PROCESS'
                message = f'Thanks for chosing us , your otp is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST["email"], ]
                send_mail( subject, message, email_from, recipient_list )
                global User_data
                User_data={
                    "username":request.POST["uname"],
                    "email":request.POST["email"],
                    "password":request.POST["password"],
                }
                return render(request,"otp.html")
            
    return render(request,"signup.html",context)

from django.contrib.auth.hashers import make_password,check_password

def otp(request):
    context={}
    if request.method=="POST":
        if otp==int(request.POST["otp"]):
            User.objects.create(
                username=User_data["username"],
                email=User_data["email"],
                password=make_password(User_data["password"]),
            )
            context["msg"]="Signup Succesfull"
            return render(request,"signup.html",context)
        else:
            context["msg"]="Invalid OTP"
    return render(request,"otp.html",context)


def login(request):
    context={}
    if request.method=="POST":
        try:
            current_user=User.objects.get(email=request.POST["email"])
            print(current_user)
            
            if check_password(request.POST["password"], current_user.password):
                context["msg"]="LOGIN SUCCESFULL"
                request.session["email"]=request.POST["email"]
                user_data=User.objects.get(email=request.session["email"])
                context["user_data"]=user_data
                return render(request,"product.html",context)
            else:
                context["msg"]="Incorrect password"
        except:
            context["msg"]="Invalid User"
    return render(request,"login.html",context)


def logout(request):
    context={}
    del request.session["email"]
    context["msg"]="LOGOUT successfull"
    return render(request,"login.html",context)

def profile(request):
    context={}
    user_data=User.objects.get(email=request.session["email"])
    context["user_data"]=user_data
    if request.method=="POST":
        user_data.username=request.POST["uname"]
        user_data.email=request.POST["email"]
        # password check
        if check_password(request.POST["opassword"],user_data.password):
            if request.POST["npassword"]==request.POST["cnpassword"]:
                user_data.password=make_password(request.POST["npassword"])
            else:
                context["user_data"]="New Password nad confirm New password Not match"
        else:
            context["user_data"]="Old Password Not match"
        
        request.FILES["propic"]
        user_data.profile_pic= request.FILES["propic"]
        
        user_data.save()
        context["msg"]="Profile Updated Successfully"
        context["user_data"]=user_data
    return render(request,"profile.html",context)

def product11(request):
     return render(request,"product11.html")
     

def product1(request):
    context={}
    user_data=User.objects.get(email=request.session["email"])
    context["user_data"]=user_data
    all_product=Product.objects.all()
    context["all_product"]=all_product
    return render(request,"product11.html",context)



def shop_cart(request):
     return render(request,"shop_cart.html")


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


def buyer(request):
    return render(request,"index.html")
def seller(request):
    return render(request,"seller.html")
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest




# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def homepage(request):
	currency = 'INR'
	amount = 20000 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url

	return render(request, 'index.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()



def cart(request, id):
    current_product = Product.objects.get(id=id)
    current_user = User.objects.get(email=request.session["email"])
    cart_exists = Cart.objects.filter(product=current_product, user=current_user)

    if cart_exists:
        cart_exists[0].quantity += 1
        cart_exists[0].total = current_product.price * cart_exists[0].quantity  # Calculate the total based on your logic
        cart_exists[0].save()
    else:
        Cart.objects.create(
            product=current_product,
            user=current_user,
            quantity=1,  # Set the initial quantity
            total=current_product.price  # Set the initial total based on your logic
        )

    return redirect("Product")


from decimal import Decimal

def cart_view(request):
    context = {}
    user_data = User.objects.get(email=request.session["email"])
    context["user_data"] = user_data

    cart_product = Cart.objects.filter(user=user_data)
    
    # Calculate subtotal for each cart item
    for cart_item in cart_product:
        cart_item.subtotal = Decimal(cart_item.product.price) * cart_item.quantity

    
    # Calculate total based on cart item subtotals
    total = sum(cart_item.subtotal for cart_item in cart_product)


    context["cart_product"] = cart_product
    context["total"] = total
    
    return render(request, "cart.html", context)

  


def view_product(request, id):
    one_data = Product.objects.get(id=id)
    context = {
        'one_data': one_data,
    }
    user_data=User.objects.get(email=request.session["email"])
    context["user_data"]=user_data
    all_product=Product.objects.all()
    context["all_product"]=all_product
    return render(request, "viewproduct.html", context)    
  


def remove_cart(request,id):
    one_cart= Cart.objects.get(id=id)   
    one_cart.delete()
    return cart_view(request)
from django.http import HttpResponseRedirect



def check_out(request):
    context = {}
    user_data = User.objects.get(email=request.session["email"])
    context["user_data"] = user_data
    
    cart_product = Cart.objects.filter(user=user_data)
    
    # Calculate subtotal for each cart item
    total_quantity = 0
    for cart_item in cart_product:
        cart_item.subtotal = Decimal(cart_item.product.price) * cart_item.quantity
        total_quantity += cart_item.quantity
    
    # Calculate total based on cart item subtotals
    total = sum(cart_item.subtotal for cart_item in cart_product)
    context["cart_product"] = cart_product
    context["total"] = total
    context["total_quantity"] = total_quantity
    
    if request.method == "POST":
        try:
            global shipping_data
            shipping_data = {
                "first_name": request.POST["first_name"], 
                "last_name": request.POST["last_name"],
                "search_country": request.POST["search_country"],
                "order_address_line1": request.POST["order_address_line1"],
                "order_address_line2": request.POST["order_address_line2"],
                "order_city": request.POST["order_city"],
                "order_zipcode": request.POST["order_zipcode"],
                "order_phone": request.POST["order_phone"],
                "order_email": request.POST["order_email"],
             }
        
                # Create an instance of Orderdetail and save it
            order_detail_instance = order.objects.create(
                first_name=shipping_data["first_name"],
                last_name=shipping_data["last_name"],
                search_country=shipping_data["search_country"],
                order_address_line1=shipping_data["order_address_line1"],
                order_address_line2=shipping_data["order_address_line2"],
                order_city=shipping_data["order_city"],
                order_zipcode=shipping_data["order_zipcode"],
                order_phone=shipping_data["order_phone"],
                order_email=shipping_data["order_email"],
             )
            order_detail_instance.save()
        except:
            context["msg"]="succefully.. " 
        payment_method = request.POST.get("checkout_payment_method")

        if payment_method == 'online':
            # Redirect to the online transfer payment handler URL
         return render(request,"onlinepayment.html")
        elif payment_method == 'cash':
            # Render the order confirmation page
            return render(request, 'order_complete.html')

            
             
    
    return render(request, "checkout.html", context)


def update_cart(request):
     
     return cart(request)

def onlinepayment(request):
    context = {}
    user_data = User.objects.get(email=request.session["email"])
    context["user_data"] = user_data
    
    cart_product = Cart.objects.filter(user=user_data)
    
    # Calculate subtotal for each cart item
    for cart_item in cart_product:
        cart_item.subtotal = Decimal(cart_item.product.price) * cart_item.quantity

    
    # Calculate total based on cart item subtotals
    total = sum(cart_item.subtotal for cart_item in cart_product)
    context["cart_product"] = cart_product
    context["total"] = total

  
    return redirect(onlinepayment, context) 
    

def confirm_order(request):
    context = {}
    user_data = User.objects.get(email=request.session["email"])
    context["user_data"] = user_data
    
    cart_product = Cart.objects.filter(user=user_data)
    
    # Calculate subtotal for each cart item
    for cart_item in cart_product:
        cart_item.subtotal = Decimal(cart_item.product.price) * cart_item.quantity

    
    # Calculate total based on cart item subtotals
    total = sum(cart_item.subtotal for cart_item in cart_product)
    context["cart_product"] = cart_product
    context["total"] = total

  
    return render(request, "confirmorder.html", context)   
