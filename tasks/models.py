from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tasks_deleted = models.PositiveIntegerField(default=0)
    tasks_created = models.PositiveIntegerField(default=0)
    #def __str__(self):
    #    return self.title
    #def get_data(self, title, description, user, request):
    #    self.title = title
    #    self.description = description
    #    self.user = request.user
    #    return [self.title, self.description, self.user]



