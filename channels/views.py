from django.shortcuts import render,get_object_or_404
from .models import Channel,Subscribe
from video.models import Video

# Create your views here.
def index(request):
	channels = Channel.objects.all()
	return render(request, 'channels/index.html', {"channels":channels})

def showChannel(request,channel_id):
	channel = Channel.objects.get_object_or_404(Channel,pk=channel_id)
	channel_videos = Video.objects.filter(channel=channel)
	channel_subscribes = Subscribe.objects.filter(channel=channel)
	context = {"channel":channel,
			   "channel_videos":channel_videos,
			   "channel_subscribes":channel_subscribes}
	return render(request,"channels/showChannel.html",context)