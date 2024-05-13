from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateTask
from .models import Task


def Home(request):
    return render(request, "Home.html")

def task_view(request):
    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)
    context = {"task": task}
    
    return render(request, "task_view.html", context=context)

def task_creation(request):
    form = CreateTask()
    if request.method == "POST":
        form = CreateTask(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.user = request.user
            

            task.save()

            return redirect("/Home/task_view/")
    
    context = {"form":form}

    return render(request, "task_creation.html")

def task_delete(request, pk):

    task = Task.objects.get(id=pk)
    task.tasks_deleted += 1
    if request.method == "POST":

        task.delete()

        return redirect("task_view")


    return render(request, "task_delete.html")

def datatable(request):
    return render(request, "datatable.html")

def add_table(request):
    return render(request, "add_table.html")