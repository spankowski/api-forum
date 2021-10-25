from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from speak.views import PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='bailif')

urlpatterns = [
    path(r'', include(router.urls)),
]
