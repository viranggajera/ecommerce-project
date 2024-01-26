from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_seller.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(sellerUser)