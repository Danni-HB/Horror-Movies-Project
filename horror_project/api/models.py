from django.db import models
from django.contrib.auth.models import User
    

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    themes = models.ManyToManyField(Theme)

    def __str__(self) -> str:
        return f"{self.title}"


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_themes = models.ManyToManyField(Theme)

    def __str__(self) -> str:
        return f"{self.user}"
