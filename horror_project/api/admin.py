from django.contrib import admin
from .models import Theme, Movie, UserPreferences

admin.site.register(Theme)
admin.site.register(Movie)
admin.site.register(UserPreferences)
