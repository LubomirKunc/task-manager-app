from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("task_creation/", views.task_creation),
    path("task_view/", views.task_view, name="task_view"),
    path("task_delete/<str:pk>/", views.task_delete, name="task_delete"),
    path("datatable/", views.datatable, name="datatable"),
    path("add_table/", views.add_table)
]
