from django.contrib import admin
from expense_tracker import views
from django.urls import path,include

urlpatterns = [
    path('',views.track,name='track'),
   # path('new/',views.newpage,name ='newpage')  
]