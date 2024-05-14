from django.db import models
 
class Inventory(models.Model):
    cropName = models.CharField(max_length=100)
    cropType = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    expiryDate = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    pricePerUnit = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

 

