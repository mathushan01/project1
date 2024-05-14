from . import views
from django.contrib import admin
from django.urls import path , include
from .views import SalaryPDF  # Import the SalaryPDF view

urlpatterns = [
    path('Home',views.Home,name="Home"),

    path('addData',views.addData, name="addData"),
    path('View_Details',views.View_Details,name="View_Details"),
    path('updateData/<int:id>',views.updateData, name="updateData"),
    path('deleteData/<int:id>',views.deleteData, name="deleteData"),

    path('pay_method',views.pay_method, name="pay_method"),
    path('card_method', views.card_method , name="card_method"),

    path('add_employee_data',views.add_employee_data,name="add_employee_data"),
    path('delete_employee_data/<int:id>',views.delete_employee_data , name="delete_employee_data"),
    path('update_employee_data/<int:id>',views.update_employee_data,name="update_employee_data"),
    path('employee_update',views.employee_update,name="employee_update"),
    
    path('salary_pdf/', SalaryPDF.as_view(), name='salary_pdf'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('Admin_payment',views.Admin_payment , name='Admin_payment'),

    path('customer_view', views.customer_view , name='customer_view'),

    path('employee_salary', views.employee_salary , name="employee_salary"),
    
]