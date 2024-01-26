from django.db import models
from app_seller.models import Product








# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profile_pic = models.FileField(upload_to='images/',default="anonymous.jpg")
    
    def __str__(self):
        return self.username
    



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.product.pname

class order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    search_country = models.CharField(max_length=200)
    order_address_line1 = models.TextField(max_length=200)
    order_address_line2 = models.TextField(max_length=200)
    order_city = models.CharField(max_length=20)
    order_zipcode = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=20)
    order_email = models.CharField(max_length=20)

    
    def __str__(self):
        return self.first_name



    

    

    



    








