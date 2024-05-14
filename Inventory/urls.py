from django.urls import path
from django.contrib import admin
from . import views
 
urlpatterns= [
    path('', views.home, name='home'),
    path('view', views.index, name='index'),
    path('inventory', views.inventory, name='inventory'),
    path('addnew', views.addnew, name='addnew'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]