from django.db import models
from app_buyer.models import *
# Create your models here.

class sellerUser(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profile_pic = models.FileField(upload_to='images/',default="anonymous.jpg")


    def __str__(self) :
        return self.username 
    




class Category(models.Model):
    cname=models.CharField(max_length=200)
    cdescription=models.TextField(max_length=500)
    user=models.ForeignKey(sellerUser,on_delete=models.CASCADE)
    def __str__(self) :
        return self.cname 
    






class Product(models.Model):
    pname=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.FileField(upload_to="product/",default="anonymus.jpg")
    image1=models.FileField(upload_to="product/",default="anonymus.jpg")
    image2=models.FileField(upload_to="product/",default="anonymus.jpg")
    image3=models.FileField(upload_to="product/",default="anonymus.jpg")
    description =models.TextField(max_length=500)
    user=models.ForeignKey(sellerUser,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    
    
    

    def __str__(self) :
        return self.pname
    