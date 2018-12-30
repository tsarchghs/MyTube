from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Video)
admin.site.register(VideoLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(UserView)
admin.site.register(AnonymousView)
admin.site.register(Category)
