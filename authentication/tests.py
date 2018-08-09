from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your tests here.

class TestViews(TestCase):
	def setUp(self):
		self.user_object = User.objects.create(username="testing",
											   password="testing")
	def test_custom_login_view(self):
		url = reverse("login")
		response_get = self.client.get(url)
		self.assertEqual(response_get.status_code,200)
		response_post = self.client.post(url,data=None)
		self.assertEqual(response_post.status_code,200)
		self.assertContains(response_post,'<form method="POST"')
		"""		self.client.force_login(self.user_object)
				response_get_loggedIn = self.client.get(url)
				print(response_get_loggedIn)
				self.assertEqual(response_get_loggedIn.status_code,302)
				self.assertEqual(response_get_loggedIn.url,"/")
		"""
	def test_signUp_view(self):
		url = reverse("signUp")
		valid_data = {"username":"usernameTesting",
					  "password1":"testing3",
					  "password2":"testing3"}
		invalid_data = {"username":"usernamsdaaseTesting",
					  "password1":"testing3",
					  "password2":"testinsdadsag3"}
		response_get = self.client.get(url)
		self.assertEqual(response_get.status_code,200)
		response_valid_post = self.client.post(url,data=valid_data)
		self.assertEqual(response_valid_post.status_code,302)
		response_valid_post = self.client.post(url,data=invalid_data)
		self.assertEqual(response_valid_post.status_code,200)
		self.assertContains(response_valid_post,'<form method="POST"')
