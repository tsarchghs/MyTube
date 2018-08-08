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
		self.user_object2 = User.objects.create(username="testing2",
												password="testing2")
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
	def checkStatusCode(self,url,method,statuscode,redirectTo=""):
		if method == "POST":
			response = self.client.post(url,HTTP_USER_AGENT='Mozilla/5.0')
		elif method == "GET":
			response = self.client.get(url,HTTP_USER_AGENT='Mozilla/5.0')
		print("{} - {} - {}".format(url,response.status_code,statuscode))
		if response.status_code == 302:
			self.assertEqual(response.url,redirectTo)
		self.assertEqual(response.status_code,statuscode)

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
			self.assertEqual(response.status_code,200)
	def test_showVideo_view(self):
		url_valid = reverse("showVideo",args=[self.video_object.id])
		url_invalid = reverse("showVideo",args=[100])
		url_invalid2 = "/video/dsadas"
		self.checkStatusCode(url_valid,"GET",200)
		self.checkStatusCode(url_invalid,"GET",404)
		self.checkStatusCode(url_invalid2,"GET",404)
	def test_deleteVideo_view(self):
		url_valid = reverse("deleteVideo",args=[self.video_object.id])
		url_valid_post_redirect = reverse("index")
		url_invalid = reverse("deleteVideo",args=[100])
		url_invalid2 = "/delete/dsadas"
		self.checkStatusCode(url_valid,"GET",200)
		self.checkStatusCode(url_valid,"POST",302,url_valid_post_redirect)
		self.checkStatusCode(url_invalid,"GET",404)
		self.checkStatusCode(url_invalid2,"GET",404)
	def test_deleteComment_view(self):
		url_valid = reverse("deleteComment",args=[self.comment_object.id])
		url_valid_redirect = reverse("showVideo",args=[self.comment_object.video.id])
		url_invalid = reverse("deleteComment",args=[100])
		url_invalid2 = "/delete/comment/dsadas"
		self.checkStatusCode(url_valid,"POST",302,url_valid_redirect)
		self.checkStatusCode(url_invalid,"GET",404)
		self.checkStatusCode(url_invalid2,"GET",404)
	def test_likeVideo_view(self):
		url_valid_redirect = reverse("showVideo",args=[self.video_object.id])
		url_valid = reverse("likeVideo",args=["like",self.video_object.id])
		url_valid2 = reverse("likeVideo",args=["dislike",self.video_object.id])
		url_invalid = reverse("likeVideo",args=["dsasd",self.video_object.id])
		url_invalid2 = reverse("likeVideo",args=["like",312])
		self.checkStatusCode(url_valid,"POST",302,url_valid_redirect)
		self.checkStatusCode(url_invalid,"GET",404)
		self.checkStatusCode(url_invalid2,"GET",404)

	def test_likeComment_view(self):
		url_valid_redirect = reverse("showVideo",args=[self.video_object.id])
		url_valid = reverse("likeComment",args=["like",self.comment_object.id])
		url_valid2 = reverse("likeComment",args=["dislike",self.comment_object.id])
		url_invalid = reverse("likeComment",args=["dsasd",self.comment_object.id])
		url_invalid2 = reverse("likeComment",args=["like",999])
		self.checkStatusCode(url_valid,"POST",302,url_valid_redirect)
		self.checkStatusCode(url_invalid,"GET",404)
		self.checkStatusCode(url_invalid2,"GET",404)