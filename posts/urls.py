from urllib.parse import urlparse
from django.urls import path

from posts.api import views
urlpatterns = [
    path('func-base-view/', views.post, name='post-home'),
    path('func-base-view/<int:pk>/', views.detail, name='post-detail'),
    path('', views.HomeAPIView.as_view(), name='home'),
    path('<pk>/', views.HomeAPIView.as_view(), name='post-updated')
]