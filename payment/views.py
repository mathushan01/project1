from .models import Billing_Address#, BillingAddress
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from .forms import Payment_make_Form
from .forms import CardForm
from .models import EmployeeData
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from .models import Payment
import io

from reportlab.lib.units import inch
from django.http import HttpResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create your views here.

from pathlib import Path
import os

#BASE_DIR = Path(__file__).resolve().parent.parent

def Home(request):
    mydata=Billing_Address.objects.all()
    return render(request,"payment/Home.html" ,{'data':mydata})


def addData(request):        #127.0.0.1:8000/addData
    if request.method == 'POST':
        username = request.user.username
        firstname=request.POST['firstname']
        email=request.POST['email']
        address=request.POST['address']
        state=request.POST['state']
        zip=request.POST['zip']   

        if not firstname.isalpha():
            messages.error(request,'Name must only contain letters.')

        obj=Billing_Address()
        obj.Name=firstname
        obj.Email=email
        obj.Address=address
        obj.State=state
        obj.Zip=zip
        obj.username=username
        obj.save()

        mydata=Billing_Address.objects.all()
        return redirect('Home')
    return redirect(request,'payment/View_Details.html',{'mydata':mydata})
        
        

def View_Details(request):
    mydata=Billing_Address.objects.all()
    return render(request,'payment/View_Details.html',{'Billing_Address':mydata})

def updateData(request,id):              #127.0.0.1:8000/updateData
    mydata = Billing_Address.objects.get(id=id)
    if request.method == "POST":
        firstname=request.POST['firstname']
        print(id)
        print(firstname)
        email=request.POST['email']
        address=request.POST['address']
        state=request.POST['state']
        zip=request.POST['zip']

        mydata.Name=firstname
        mydata.Email=email
        mydata.Address=address
        mydata.State=state
        mydata.Zip=zip
        mydata.save()

        return redirect('View_Details')
    
    return render(request,"payment/update.html",{'data':mydata})

def deleteData(request,id):      #127.0.0.1:8000/deleteData
    mydata = Billing_Address.objects.get(id=id)
    mydata.delete()
    return redirect('View_Details')


def pay_method(request):
    if request.method == 'POST':
        form = Payment_make_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_success')  # Redirect to success page
    else:
        form = Payment_make_Form()
    return render(request, 'payment/pay_method.html', {'form': form})



def card_method(request):
    if request.method == 'POST':
        form = CardForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_method')  # Redirect to success page
    else:
        form = CardForm()
    return render(request,"payment/card_method.html" , {'form': form})    


def Admin_payment(request):
    return render(request,'payment/Admin_payment.html')

def customer_view(request):
    username = request.user.username
    data = Billing_Address.objects.filter(username=username)
    if data is not None:
        return render(request, "payment/customer_view.html",{"data":data})
    
    return render(request, "payment/customer_view.html")
def add_employee_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        card_number = request.POST['card_number']
        amount = request.POST['amount']
        date = request.POST['date']

        obj = EmployeeData()
        obj.name = name
        obj.card_number = card_number
        obj.amount = amount
        obj.date = date
        obj.save()
        empData = EmployeeData.objects.all()
        return redirect('employee_salary')
    return redirect(request,'employee_salary.html' ,{'empData' : empData} )

def employee_salary(request):
    print("hello")
    empData = EmployeeData.objects.all()
    return render(request,"payment/employee_salary.html",{'EmployeeData':empData})

def delete_employee_data(request,id):      #127.0.0.1:8000/deleteData
    empData = EmployeeData.objects.get(id=id)
    empData.delete()
    return redirect('employee_salary')

def update_employee_data(request,id):
    empData = EmployeeData.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        print(id)
        print(name)
        card_number = request.POST['card_number']
        amount = request.POST['amount']
        date = request.POST['date']

        empData.name = name
        empData.card_number = card_number
        empData.amount = amount
        empData.date = date
        empData.save()

        return redirect('employee_salary')
    return render(request,"payment/employee_update.html",{'employee':empData})

def employee_update(request):
    return render(request,"employee_update.hrml")

class SalaryPDF(View):
    def get(self, request, *args, **kwargs):
        buf = io.BytesIO()

        # Create a canvas
        c = canvas.Canvas(buf, pagesize=letter)
        
        # Set font and text origin
        c.setFont("Helvetica", 14)
        text_x, text_y = 100, 750  # Adjust coordinates as needed

        # Retrieve Billing_Address data from the database
        datas = Billing_Address.objects.all()

        # Set CSS styles
        c.setFont("Helvetica", 12)
        styles = c.beginText(text_x, text_y)
        styles.setFont("Helvetica", 12)
        styles.setTextOrigin(text_x, text_y)

        # Write Billing details to the PDF
        for data in datas:
            Name = data.Name
            Email = data.Email
            Address = data.Address
            State = data.State
            Zip = data.Zip
            
            # Define the text content with CSS styles
            text_content = f"Name: {Name}\nEmail: {Email}\nAddress: {Address}\nState: {State}\nZip: {Zip}\n\n"
            styles.textLines(text_content)

        # Draw text with styles
        c.drawText(styles)

        # Save and close the canvas
        c.save()
        buf.seek(0)

        # Prepare HTTP response with the PDF as an attachment
        response = HttpResponse(buf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="salary_details.pdf"'
        return response
    

