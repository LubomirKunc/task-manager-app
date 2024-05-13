from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect("/")
    return render(request, "Login.html")

def Registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        age = request.POST["age"]
        lname = request.POST["lname"]
        fname = request.POST["fname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request, "Username Already exists!!! Kindly, use another one.")
            return redirect("/")
        if User.objects.filter(email=email):
            messages.error(request, "Email Already registred!!! Kindly, use another one.")
            return redirect("/")
        if len(username) > 15:
            messages.error(request, "Username too long!")
            return redirect("/")
        if pass1 != pass2:
            messages.error(request, "The passwords don't match!")
            return redirect("/")
        if username.isnumeric() == True:
            messages.error(request, "Username can't be all number!")
            return redirect("/")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.age = age

        myuser.save()

        messages.success(request, "Your account has been succesfully created")

        return redirect("/Login/")
    return render(request, "Registration.html")

def Logout(request):
    logout(request)
    messages.success(request, "Logged out succesfully!")
    return redirect("/")

def index(request):
    return render(request, "index.html")

def Chart(request):
    data = []
    labels = []

    queryset = User.objects.order_by("-username")[:5]
    for request.user in queryset:
        labels.append(User.username)
        data.append(UserProfile.age)
    return render(request, "Chart.html", {
        "labels": labels,
        "data": data
    })