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
	def test_views_200(self):
		pathname_args = {"index":[],
						 "showVideo":[self.video_object.id],
						 "createVideo":[],
						 "editVideo":[self.video_object.id],
						 "createComment":[self.video_object.id],
						 "editComment":[self.comment_object.id]}
		for pathname,args in pathname_args.items():
			url = reverse(pathname,args=args)
			response = self.client.get(url,HTTP_USER_AGENT='Mozilla/5.0') #HTTP_USER_AGENT needed for showVideo view
			print(url)
			print(response)
			self.assertEqual(response.status_code,200)
	def test_showVideo_view(self):
		url_valid = reverse("showVideo",args=[self.video_object.id])
		response = self.client.get(url_valid,HTTP_USER_AGENT='Mozilla/5.0')
		self.assertEqual(response.status_code,200)
		url_invalid = reverse("showVideo",args=[100])
		response1 = self.client.get(url_invalid,HTTP_USER_AGENT='Mozilla/5.0')
		self.assertEqual(response1.status_code,404)
		url_invalid2 = "/video/dsadas"
		response2 = self.client.get(url_invalid2,HTTP_USER_AGENT='Mozilla/5.0')
		self.assertEqual(response2.status_code,404)