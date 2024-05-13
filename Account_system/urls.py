from django.urls import path, include
from . import views

urlpatterns = [
    path("Login/", views.Login),
    path("Registration/", views.Registration),
    path("Home/", include("tasks.urls")),
    path("", views.index),
    path("Logout/", views.Logout),
    path("Chart/", views.Chart, name="Chart")
]
