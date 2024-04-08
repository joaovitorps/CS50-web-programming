from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def john(request):
    return HttpResponse("yo john")


def greet(request, name):
    return HttpResponse(f"Yoooo {name.capitalize()}")


def greet1(request, name):
    context = {"name": name.capitalize()}
    return render(request, "hello/greet1.html", context)


def user(request, id):
    return HttpResponse(f"This is the user id: {id}".title())
