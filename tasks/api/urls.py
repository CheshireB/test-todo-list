from django.contrib import admin
from django.urls import path, include


from .views import (
    TaskListView,
    TaskAPIView,
    TaskCreateAPIView,
)


urlpatterns = [
    path('list/', TaskListView.as_view()),
    path('<int:pk>/', TaskAPIView.as_view()),
    path('', TaskCreateAPIView.as_view()),
]