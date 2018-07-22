from django import forms
from .models import *

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		exclude = ["channel"]

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["content"]