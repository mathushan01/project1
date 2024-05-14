from django.shortcuts import render, redirect

from Inventory.forms import InventoryForm
from Inventory.models import Inventory

# Create your views here.

def home(request):
    return render(request, 'Inventory/test.html')

def inventory(request):
    return render(request, 'Inventory/inventory.html')


def index(request):
    inventories = Inventory.objects.all()
    return render(request, "Inventory/show.html", {'inventories': inventories})
 
def addnew(request):
    if request.method == "POST":
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Inventory/view')
    else:
        form = InventoryForm()
    return render(request, "Inventory/index.html", {'form': form})
 
 
def edit(request, id):
    inventory = Inventory.objects.get(id=id)
    return render(request, "Inventory/edit.html", {'inventory': inventory})
 
def update(request, id):  
    inventory = Inventory.objects.get(id=id)  
    form = InventoryForm(request.POST, request.FILES, instance = inventory)  
    print(form.is_valid())
    if form.is_valid():  
        form.save()  
        return redirect("/Inventory/view")  
    return render(request, 'Inventory/edit.html', {'inventory': inventory})
 
def destroy(request, id):  
    inventory =Inventory.objects.get(id=id)  
    inventory.delete()  
    return redirect("/Inventory/view")



