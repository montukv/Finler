from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('emicalc',views.emicalc,name='emicalc'),
]