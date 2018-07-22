from django.shortcuts import render,redirect,reverse
from channels.models import Channel
from .models import Video,VideoLike,Comment,CommentLike
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collections import OrderedDict
# Create your views here.

def showVideo(request,video_id):
	video = Video.objects.get(pk=video_id)
	video_likes = len(VideoLike.objects.filter(video=video,like=True,dislike=False))
	video_dislikes = len(VideoLike.objects.filter(video=video,like=False,dislike=True))
	video_comments = Comment.objects.filter(video=video).order_by("-id")
	comment_likes = OrderedDict()
	for comment in video_comments:
		likes = CommentLike.objects.filter(comment=comment,like=True,dislike=False)
		dislikes = CommentLike.objects.filter(comment=comment,like=False,dislike=True)		
		comment_likes[comment] = len(likes) - len(dislikes)
	context = {"video":video,
			   "video_likes":video_likes-video_dislikes,
			   "comment_likes":comment_likes,			   
			   }
	return render(request,"video/showMovie.html",context)


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