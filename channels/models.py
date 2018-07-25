from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)



    def __str__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)

    def __unicode__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)

def Subscribe(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	channel = models.ForeignKey(Channel,on_delete=models.CASCADE)