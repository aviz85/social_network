# social_network/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('users.urls')),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]

# Add this if you're using media files (e.g., for profile pictures)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)