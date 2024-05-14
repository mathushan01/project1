from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Billing_Address(models.Model):
    username = models.CharField(max_length=100)
    Name = models.CharField(max_length=100 , default='')
    Email = models.CharField(max_length=100 , default='')
    Address = models.CharField(max_length=100, default='')
    State = models.CharField(max_length=100 , default='')
    Zip = models.IntegerField(default='')

'''
class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name'''
    

class Payment(models.Model):
    bank_receipt = models.ImageField(upload_to='bank_receipts/')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment #{self.id}'

class EmployeeData(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Card(models.Model):
    cardNumber = models.CharField(max_length=16)
    expiryDate = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f'Payment - Card ending in {self.card_number[-4:]}'