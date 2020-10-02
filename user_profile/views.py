from django.shortcuts import render
from .models import UserProfile
# Create your views here.
def showProfile(request):
	profile = UserProfile.objects.get(user=request.user)
	context = {"user_profile":profile}
	return render(request,"user_profile/profile.html",context)
