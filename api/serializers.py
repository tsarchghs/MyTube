from rest_framework import serializers
from video.models import Comment
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from video.models import Video,Category
from user_channel.models import UserChannel

class UserChannelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserChannel
		exclude = []

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		exclude = []

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		exclude = []

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		exclude = []

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserProfile
		exclude = []

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		exclude = []