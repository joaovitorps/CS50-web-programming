from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        url = reverse("users:login")
        return HttpResponseRedirect(url)

    context = {"user": request.user}
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            url = reverse("users:index")
            return HttpResponseRedirect(url)
        else:
            context = {"message": "Invalid Credentials"}
            return render(request, "users/login.html", context)

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    context = {"message": "Logged Out"}
    return render(request, "users/login.html", context)
