from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users",views.ViewUsers)
router.register("user_profiles",views.ViewUserProfiles)
router.register("user_channels",views.ViewUserChannels)
router.register("videos",views.ViewVideos)
router.register("comments",views.ViewComments)

urlpatterns = [
	path("",include(router.urls)),
	path("validate_credentials/",views.ValidateCredentials.as_view(),name="validate_credentials"),
	path("like_video/",views.LikeVideo.as_view(),name="like_video"),
	path("get_current_user_profile/",views.GetCurrentUserProfile.as_view(),name="get_current_user_profile"),
]