from django.test import TestCase
from django.shortcuts import reverse
from .models import Video,Comment
from channels.models import Channel
from django.contrib.auth.models import User
from django.core.files.base import File
# Create your tests here.

class TestViews(TestCase):
	def setUp(self):
		videoFile = open("video.mp4","r")
		photoFile = open("photo.png","r")
		self.user_object = User.objects.create(username="testing",
											   password="testing")
		self.channel_object = Channel.objects.create(user=self.user_object,
													 name="testing",
													 description="testing",
													 photo=File(photoFile))
		self.video_object = Video.objects.create(channel=self.channel_object,
												 video_file=File(videoFile),
												 title="testing",
												 description="testing")
		self.comment_object = Comment.objects.create(user=self.user_object,
													 video=self.video_object,
													 content="testing")
		self.client.force_login(self.user_object)
