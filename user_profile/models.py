from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="profile_photos/")
	phone = models.IntegerField()
	def __str__(self):
		return self.user.username + " - profile"