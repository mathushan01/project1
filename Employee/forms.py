from django import forms
from Employee.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstName', 'lastName', 'empID', 'basicSalary', 'age','phoneNumber','position','gender']
        widgets = {'firstName': forms.TextInput(attrs={'class': 'form-control'}),
                   'lastName': forms.TextInput(attrs={'class': 'form-control'}),
                   'empID': forms.TextInput(attrs={'class': 'form-control'}),
                   'basicSalary': forms.TextInput(attrs={'class': 'form-control'}),
                   'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
                   'position': forms.TextInput(attrs={'class': 'form-control'}),
                   'gender': forms.TextInput(attrs={'class': 'form-control'}),
                   }

