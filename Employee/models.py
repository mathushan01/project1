from django.db import models
 
class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    empID = models.CharField(max_length=100)
    basicSalary = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
 