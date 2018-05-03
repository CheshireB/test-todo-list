from django.contrib import admin
from django.urls import path, include


from .views import (
    TaskListView,
    TaskAPIView,
)


urlpatterns = [
    path('list/', TaskListView.as_view()),
    path('<int:pk>/', TaskAPIView.as_view())
]