from rest_framework import serializers
from video.models import Comment
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from video.models import Video

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		exclude = []

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		exclude = []
