from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="channel_image")


    def __str__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)

    def __unicode__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)

class Subscribe(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	user_channel = models.ForeignKey(UserChannel,on_delete=models.CASCADE)