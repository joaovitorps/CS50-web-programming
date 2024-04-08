from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(response):
    now = datetime.now()
    return render(
        response, "newyear/index.html", {"newyear": now.month == 1 and now.day == 1}
    )
