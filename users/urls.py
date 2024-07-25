# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='user-register'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]