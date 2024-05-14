from django import forms
from .models import Payment
from .models import EmployeeData
from .models import Card

class Payment_make_Form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bank_receipt']

class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = ['name', 'card_number', 'amount', 'date']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['cardNumber', 'expiryDate', 'cvv']        