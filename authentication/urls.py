from django.urls import path,include
from . import views

urlpatterns = [
	path("login",views.custom_login,name="login"),
	path("signup",views.signUp,name="signUp"),
	path("", include('django.contrib.auth.urls')),
]
