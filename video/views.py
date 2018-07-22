from django.shortcuts import render,redirect,reverse
from channels.models import Channel
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
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

@login_required
def editVideo(request,video_id):
	current_user = request.user
	video = Video.objects.get(pk=video_id)
	if video.channel.user == current_user:
		if request.method == "POST":
			form = VideoForm(request.POST,request.FILES,instance=video)
			if form.is_valid():
				video = form.save(commit=False)
				video.save()
				return redirect(reverse("editVideo",args=[video_id]))
			else:
				return render(request,"video/editVideo.html",{"form":form})
		else:
			form = VideoForm(instance=video)
			return render(request,"video/editVideo.html",{"form":form,"video":video})
	else:
		raise Http404

@login_required
def deleteVideo(request,video_id):
	current_user = request.user
	video = Video.objects.get(pk=video_id)
	if video.channel.user == current_user:
		if request.method == "POST":
			video.delete()
			return redirect("/video/")
		else:
			return render(request,"video/delete_video_confirmation.html",{"video":video})
	else:
		raise Http404