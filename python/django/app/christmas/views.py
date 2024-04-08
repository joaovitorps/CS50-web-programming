from django.shortcuts import render
from datetime import datetime

# Create your views here.


def today():
    today = datetime.now()
    return today


def is_christmas(today=today()):
    is_christmas = False

    if today.day == 25 and today.month == 12:
        is_christmas = True

    context = {"is_christmas": is_christmas}
    return context


def index(request):
    context = is_christmas()

    return render(request, "christmas/index.html", context)
