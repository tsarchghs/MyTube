from django.db import models
from channels.models import Channel
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import mimetypes

def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext

VIDEO = tuple(get_extensions_for_type('video'))

class Video(models.Model):
	channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	video_file = models.FileField(upload_to="videos",
		validators=[FileExtensionValidator(allowed_extensions=VIDEO)])
	title = models.CharField(max_length=300)
	description = models.TextField()

class VideoLike(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	video = models.ForeignKey(Video,on_delete=models.CASCADE)
	like = models.BooleanField()
	dislike = models.BooleanField()

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	video = models.ForeignKey(Video,on_delete=models.CASCADE)
	content = models.TextField()

	def __str__(self):
		if len(self.content) < 300:
			return content
		else:
			return content[300:] + "..."

class CommentLike(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
	like = models.BooleanField()
	dislike = models.BooleanField()
