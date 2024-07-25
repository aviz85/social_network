# social_network/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]

# posts/urls.py
from django.urls import path
from .views import PostList

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
]