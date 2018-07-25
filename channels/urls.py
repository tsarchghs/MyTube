from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="channelIndex"),
    path("<channel_id>",views.showChannel,name="showChannel"),
]
