from django import forms
from .models import *

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		exclude = ["channel"]