from django.shortcuts import render,redirect,reverse
from channels.models import Channel
from .forms import VideoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def createVideo(request):
	current_user = request.user
	user_channel = Channel.objects.filter(user=current_user)
	if user_channel:
		user_channel = Channel.objects.get(user=current_user)
		if request.method == "POST":
			form = VideoForm(request.POST,request.FILES)
			if form.is_valid():
				video = form.save(commit=False)
				video.channel = user_channel
				video.save()
				return redirect(reverse("createVideo"))
			else:
				return render(request,"video/createVideo.html",{"form":form})
		else:
			form = VideoForm()
			return render(request,"video/createVideo.html",{"form":form})
	else:
		pass #show you don't have a channel page