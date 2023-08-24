from cryptography.fernet import Fernet
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User, password
import json


def index(request):
    if request.user.is_authenticated:
        passwords = password.objects.filter(owner=request.user)
        return render(request, "vault/mainuserpage.html",{
            "passwords": passwords
        })
    else:
        return render(request, "vault/aboutus.html")


def about_us(request):
    return render(request, "vault/aboutus.html")


def add_password(request):
    if request.method == "GET":
        return render(request, "vault/addpassword.html")

    if request.method == "POST":
        title = request.POST["title"]
        website = request.POST["website"]
        masterkey = request.POST["masterkey"]
        notes = request.POST["description"]
        thepassword = request.POST["password"]
        #change string of master-key to bytes
        masterkey_bytes = masterkey.encode('utf-8')
        #Make the fernet object using that master-key in bytes
        fernet = Fernet(masterkey_bytes)
        encrypted_password = fernet.encrypt(thepassword.encode())
        #change to bytes so that decoding later on works
        encrypted_bytes = encrypted_password.decode('utf-8')
        apassword = password(
            title=title,
            website=website,
            notes=notes,
            hashed_password=encrypted_bytes,
            owner=request.user)
        apassword.save()
        return HttpResponseRedirect(reverse("index"))


def delete_password(request):
    if request.method == "POST":
        id = request.POST["id"]
        password.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse("index"))


def reveal(request, id):
    if request.method == "POST":
        info = json.loads(request.body)
        masterkey = info["masterkey"]
        encrypted_password = password.objects.get(id=id).hashed_password
        # Master-key in bytes
        bytes_data = masterkey.encode('utf-8')
        # if masterkey is short
        try:
            fernet = Fernet(bytes_data)
        except ValueError:
            return JsonResponse({"password": "There is an error in the program"})
        # if masterkey is wrong invalid token gets raised by library
        try:
            decrypted_password = fernet.decrypt(encrypted_password).decode()
        except:
            decrypted_password = 'There is an error in the program'
        return JsonResponse({"password": decrypted_password})


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
