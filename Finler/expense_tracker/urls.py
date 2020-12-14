from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('expensetracker',views.expensetracker,name='expensetracker'),
    path('add_item',views.add_item,name='add item')
]