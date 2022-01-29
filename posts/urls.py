from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from posts.api import views
urlpatterns = [
    # function base view
    path('func-base-view/', views.post, name='post-home'),
    path('func-base-view/<int:pk>/', views.detail, name='post-detail'),
    # Simple APIView
    # path('post-api/', views.HomeAPIView.as_view(), name='home'),
    # path('<pk>/', views.HomeAPIView.as_view(), name='post-updated'),

    # APIs class base view
    path('', views.ListAPIsView.as_view(), name='api-list'),
    path('create/', views.CreateView.as_view(), name='create-api'),
    path('detail/<pk>/', views.DetailAPIView.as_view(), name='detail-api'),
    path('update/<pk>/', views.UpdateAPIView.as_view(), name='update-api'),
    path('delete/<pk>/', views.DeleteAPIView.as_view(), name='delete-api')

]

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

urlpatterns += router.urls
