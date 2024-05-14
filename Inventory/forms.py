from django import forms
from Inventory.models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['cropName', 'cropType', 'image', 'quantity', 'expiryDate', 'supplier', 'pricePerUnit', 'status']
        widgets = {
            'cropName': forms.TextInput(attrs={'class': 'form-control', 'oninput': 'validateCropName(event)'}),
            'cropType': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'oninput': 'validateQuantity(event)'}),
            'expiryDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
            'pricePerUnit': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}), 
        }