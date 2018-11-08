from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('auth/', include("authentication.urls")),
	path('channel/', include('user_channel.urls')),
	path('video/',include('video.urls')),
	path('',include('home.urls')),
	path('api/', include(('api.urls',"api"),namespace="api")),
	path('api-auth/', include('rest_framework.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
