from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users",views.ViewUsers)
router.register("user_profiles",views.ViewUserProfiles)
router.register("user_channels",views.ViewChannels)
router.register("videos",views.ViewVideos)
router.register("comments",views.ViewComments)

urlpatterns = [
	path("",include(router.urls)),
	path("validate_credentials/",views.ValidateCredentials.as_view(),name="validate_credentials"),
]