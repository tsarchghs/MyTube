from django.shortcuts import render,redirect,reverse,get_object_or_404
from channels.models import Channel
from .models import Video,VideoLike,Comment,CommentLike,UserView,AnonymousView
from .forms import VideoForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collections import OrderedDict
# Create your views here.

def index(request):
	video_views = {}
	videos = Video.objects.all()
	for video in videos:
		anonViews = len(AnonymousView.objects.filter(video=video))
		userViews = len(UserView.objects.filter(video=video))
		video_views[video] = anonViews + userViews
	context = {"video_views":video_views}
	return render(request,"video/index.html",context)


def showVideo(request,video_id):
	user_agent = request.META['HTTP_USER_AGENT']
	video = get_object_or_404(Video,pk=video_id)
	if request.user.is_authenticated:
		UserView.objects.create(user=request.user,browser=user_agent,video=video)
	else:
		AnonymousView.objects.create(browser=user_agent,video=video)
	userViews = UserView.objects.filter(video=video)
	anonymousViews = AnonymousView.objects.filter(video=video)
	video_likes = len(VideoLike.objects.filter(video=video,like=True,dislike=False))
	video_dislikes = len(VideoLike.objects.filter(video=video,like=False,dislike=True))
	video_comments = Comment.objects.filter(video=video).order_by("-id")
	comment_likes = OrderedDict()
	for comment in video_comments:
		likes = CommentLike.objects.filter(comment=comment,like=True,dislike=False)
		dislikes = CommentLike.objects.filter(comment=comment,like=False,dislike=True)		
		comment_likes[comment] = len(likes) - len(dislikes)
	context = {"video":video,
			   "video_likes":video_likes,
			   "video_dislikes":video_dislikes,
			   "comment_likes":comment_likes,
			   "views":len(userViews)+len(anonymousViews)   
			   }
	return render(request,"video/showVideo.html",context)


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
				return render(request,"video/video_form.html",{"action":"Create","form":form})
		else:
			form = VideoForm()
			return render(request,"video/video_form.html",{"action":"Create","form":form})
	else:
		return render(request,"video/channel_not_found.html")

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
				return render(request,"video/video_form.html",{"action":"Edit","form":form})
		else:
			form = VideoForm(instance=video)
			return render(request,"video/video_form.html",{"action":"Edit","form":form,"video":video})
	else:
		raise Http404

@login_required
def deleteVideo(request,video_id):
	current_user = request.user
	video = get_object_or_404(Video,pk=video_id)
	if video.channel.user == current_user:
		if request.method == "POST":
			video.delete()
			return redirect("/video/")
		else:
			return render(request,"video/delete_video_confirmation.html",{"video":video})
	else:
		raise Http404

@login_required
def deleteComment(request,comment_id):
	comment = get_object_or_404(Comment,pk=comment_id)
	video_id = comment.video.id
	if comment.user == request.user:
		comment.delete()
	return redirect(reverse("showVideo",args=[video_id]))

@login_required
def likeVideo(request,type_,video_id):
	if type_ not in ["like","dislike"]:
		raise Http404
	current_user = request.user
	video = get_object_or_404(Video,pk=video_id)
	userLiked = VideoLike.objects.filter(video=video,user=current_user,like=True,dislike=False)
	userDisliked = VideoLike.objects.filter(video=video,user=current_user,like=False,dislike=True)
	if not userLiked:
		if type_ == "like":
			if userDisliked:
				userDislike = VideoLike.objects.get(video=video,user=current_user,like=False,dislike=True)
				userDislike.delete()
			VideoLike.objects.create(video=video,user=current_user,like=True,dislike=False)
	elif not userDisliked:
		if type_ == "dislike":
			if userLiked:
				userLike = VideoLike.objects.get(video=video,user=current_user,like=True,dislike=False)
				userLike.delete()
			VideoLike.objects.create(video=video,user=current_user,like=False,dislike=True)
	return redirect(reverse("showVideo",args=[video_id]))

@login_required
def likeComment(request,type_,comment_id):
	if type_ not in ["like","dislike"]:
		raise Http404
	current_user = request.user
	comment = get_object_or_404(Comment,pk=comment_id)
	userLiked = CommentLike.objects.filter(comment=comment,user=current_user,like=True,dislike=False)
	userDisliked = CommentLike.objects.filter(comment=comment,user=current_user,like=False,dislike=True)
	if not userLiked:
		if type_ == "like":
			if userDisliked:
				likeObj = CommentLike.objects.get(comment=comment,user=current_user,like=False,dislike=True)
				likeObj.delete()
			CommentLike.objects.create(comment=comment,user=current_user,like=True,dislike=False)
	if not userDisliked:
		if type_ == "dislike":
			if userLiked:
				dislikeObj = CommentLike.objects.get(comment=comment,user=current_user,like=True,dislike=False)
				dislikeObj.delete()
			CommentLike.objects.create(comment=comment,user=current_user,like=False,dislike=True)
	return redirect(reverse("showVideo",args=[comment.video.id]))

@login_required
def createComment(request,video_id):
	current_user = request.user
	video = get_object_or_404(Video,pk=video_id)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.video = video
			comment.save()
			return redirect(reverse("showVideo",args=[video.id]))
		else:
			return render(request,"video/comment_form.html",{"action":"Create","form":form})
	else:
		form = CommentForm()
		return render(request,"video/comment_form.html",{"action":"Create","form":form})

@login_required
def editComment(request,comment_id):
	current_user = request.user
	try:
		comment = Comment.objects.get(pk=comment_id)
	except:
		raise Http404
	if request.method == "POST":
		form = CommentForm(request.POST,instance=comment)
		if form.is_valid():
			comment.save()
			return redirect(reverse("showVideo",args=[comment.video.id]))
		else:
			return render(request,"video/comment_form.html",{"action":"Edit","form":form})
	else:
		form = CommentForm(instance=comment)
		return render(request,"video/comment_form.html",{"action":"Edit","form":form})