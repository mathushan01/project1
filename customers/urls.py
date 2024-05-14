from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.login_signup ,name ="login_signup"),
    path('account',views.account ,name ="account"),
    path('checkCode',views.checkCode ,name ="checkCode"),
    path('totalViews',views.totalViews,name='totalViews'),
    path('totalFarmerRequestGrouth',views.totalFarmerRequestGrouth,name='totalFarmerRequestGrouth'),
    path('totalProductsGrouth',views.totalProductsGrouth,name='totalProductsGrouth'),
    path('removeUser',views.removeUser,name='removeUser'),
    path('overView',views.overView,name='overView'),
    path('adminCustomer',views.adminCustomer,name='adminCustomer'),
    path('addItems',views.addItems,name='addItems'),
    path('graphView',views.graphView,name='graphView'),
    path('products_sell',views.products_sell,name='products_sell'),
    path('payment/<str:name>',views.payment,name='payment'),
    path('addToCart/<str:name>',views.addToCart,name='addToCart'),
    path('about',views.about,name='about'),
    path('aboutd/<str:name>',views.aboutd,name='aboutd'),
    path('farmerRequest',views.farmerRequest,name='farmerRequest'),
]