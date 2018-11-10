from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from video.models import Comment
from .serializers import CommentSerializer,UserProfileSerializer,UserSerializer,VideoSerializer,ChannelSerializer
from user_profile.models import UserProfile
from video.models import Video
from user_channel.models import Channel
# Create your views here.

class ValidateCredentials(APIView):
	permission_classes = []
	def get(self,request):
		content = {"post_only":True}
		return Response(content)
	def post(self,request):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username,password=password)
		if user is not None:
			content = {"valid_credentials":True}
		else:
			content = {"valid_credentials":False}
		return Response(content)

class ViewChannel(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer

class ViewVideos(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
	
class ViewUsers(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ViewUserProfiles(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class ViewComments(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer