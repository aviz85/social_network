# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('posts/<int:pk>/like/', views.toggle_like, name='toggle-like'),
]