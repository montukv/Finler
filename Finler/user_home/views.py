from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"user_home/home.html")

def profile(request):
    return render(request,"user_home/profile.html")
 