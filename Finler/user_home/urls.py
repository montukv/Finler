from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('user_home_dashboard',views.user_home_dashboard,name='user_home_dashboard')
]