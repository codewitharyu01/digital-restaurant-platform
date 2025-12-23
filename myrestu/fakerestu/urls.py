
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path("feedback/",feedback), 
   
   path("order/",order),
   path("table/",resto_table,name='table_booking'),
   path("dilivered/",food_dilivered,name='diliver'),
   path("logout/",logout,name='logout')
   
   
   
]

