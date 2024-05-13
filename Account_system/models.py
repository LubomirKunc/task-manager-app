from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.TextField()
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.username