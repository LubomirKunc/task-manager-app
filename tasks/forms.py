from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Task

class CreateTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "description",]
        exclude = ["user",]