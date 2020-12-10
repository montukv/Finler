from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from .forms import expenseform
from .models import expense
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required

def track(request):
	obj = None
	if request.method=="POST":
		user = request.POST["username"]
		name = request.POST["name"]
		cost = request.POST["cost"]
		date = request.POST["date"]

		data = expense(username=user,name=name,cost=cost,date=date)
		data.save()
		obj = expense.objects.all()
	return render(request,'expense_tracker/track.html',{'obj':obj})

#def expense_detail(request):
#	obj = expense.objects.all()
#	return render(request,'expense_tracker/index.html',{'obj':obj})

