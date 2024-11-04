from rest_framework import viewsets
from .models import Movie, Theme, UserPreferences
from .serializers import UserSerializer, MovieSerializer, ThemeSerializer, UserPreferencesSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Movie ViewSet
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Theme ViewSet
class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

# User Preferences ViewSet
class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer

    @action(detail=True, methods=['get'])
    def preferences(self, request, pk=None):
        user_preferences = self.get_object()
        serializer = UserPreferencesSerializer(user_preferences)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def save_preferences(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserPreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
