from django.contrib import admin

from payment.models import Billing_Address, EmployeeData, Payment , Card

# Register your models here.
admin.site.register(EmployeeData)
admin.site.register(Billing_Address)
admin.site.register(Payment)
admin.site.register(Card)