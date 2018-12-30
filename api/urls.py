from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users",views.UsersViewSet)
router.register("user_profiles",views.UserProfilesViewSet)
router.register("user_channels",views.UserChannelsViewSet)
router.register("videos",views.VideosViewSet)
router.register("comments",views.CommentsViewSet)

urlpatterns = [
	path("",include(router.urls)),
	path("validate_credentials/",views.ValidateCredentials.as_view(),name="validate_credentials"),
	path("like_video/",views.LikeVideo.as_view(),name="like_video"),
	path("get_current_user_profile/",views.GetCurrentUserProfile.as_view(),name="get_current_user_profile"),
	path("filter_comments/<int:video_id>/<int:from_>/<int:to_>",views.FilterComments.as_view(),name="filter_comments"),
]