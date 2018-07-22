from django.urls import path
from . import views

urlpatterns = [
	path("<video_id>",views.showVideo,name="showVideo"),
	path("create",views.createVideo,name="createVideo"),
	path("edit/<video_id>",views.editVideo,name="editVideo"),
	path("delete/<video_id>",views.deleteVideo,name="deleteVideo"),
	path("<type_>/video/<video_id>",views.likeVideo,name="likeVideo"),
]
