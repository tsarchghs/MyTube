from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)

    def __unicode__(self):
        return "{user}, created channel: '{name}'".format(name=self.name, user=self.user)
