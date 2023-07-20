from cryptography.fernet import Fernet
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


def index(request):
    if request.user.is_authenticated:
        return render(request, "vault/mainuserpage.html")
    else:
        return render(request, "vault/aboutus.html")


def about_us(request):
    return render(request, "vault/aboutus.html")


def add_password(request):
    if request.method == "GET":
        return render(request, "vault/addpassword.html")


def login_after_register(request):
    login(request, request.user)
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "vault/login.html", {
                "message": "Invalid username and/or password.",
            })
    else:

        return render(request, "vault/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "vault/register.html", {
                "message": "Passwords must match.",
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "vault/register.html", {
                "message": "Username already taken.",
            })
        key = Fernet.generate_key()
        string_key = key.decode('utf-8')
        return render(request, "vault/masterkey.html", {
            "masterkey": string_key,
        })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "vault/register.html")
