from django import template
from user_profile.models import UserProfile
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='getProfile')
def getProfile(user_id):
	user = User.objects.get(pk=user_id)
	return UserProfile.objects.get(user=user).id

