from django import forms
from .models import *

class VideoForm(forms.Form):
	class Meta:
		model = Video
		#fields generates a list of all editable fields of Student model
		fields = [f.name for f in Video._meta.get_fields() if not f.name in ["created","modified"]]