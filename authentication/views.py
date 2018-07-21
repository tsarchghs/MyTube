from django.shortcuts import render,redirect
from django.contrib.auth.views import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def custom_login(request,**kwargs):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		return login(request)

def signUp(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/auth/login')
		else:
			return render(request,"registration/signUp.html",{"form":form})
	else:
		form = UserCreationForm()
		return render(request,"registration/signUp.html",{"form":form})
