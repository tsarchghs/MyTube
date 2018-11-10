from django.urls import path
from . import views

urlpatterns = [
	path("",views.index,name="index"),
	path("<int:video_id>",views.showVideo,name="showVideo"),
	path("create/video",views.createVideo,name="createVideo"),
	path("create/comment/<int:video_id>",views.createComment,name="createComment"),
	path("edit/video/<int:video_id>",views.editVideo,name="editVideo"),
	path("edit/comment/<int:comment_id>",views.editComment,name="editComment"),
	path("delete/<int:video_id>",views.deleteVideo,name="deleteVideo"),
	path("delete/comment/<int:comment_id>",views.deleteComment,name="deleteComment"),
	path("<str:type_>/comment/<int:comment_id>",views.likeComment,name="likeComment"),
]
