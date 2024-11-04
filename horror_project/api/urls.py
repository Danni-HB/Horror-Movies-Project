from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MovieViewSet, ThemeViewSet, UserPreferencesViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'preferences', UserPreferencesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
