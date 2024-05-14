from django.contrib import admin
from .models import CartBox, CustomUser, FarmerRequests, UserMessages
from .models import Products
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Products)
admin.site.register(CartBox)
admin.site.register(UserMessages)
admin.site.register(FarmerRequests)