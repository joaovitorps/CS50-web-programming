from django.shortcuts import render
from datetime import datetime

# Create your views here.


def is_christmas(request):
    is_christmas = False
    today = datetime.today().strftime("%m-%d")

    if today == "12-25":
        is_christmas = True

    context = {"is_christmas": is_christmas}

    return render(request, "christmas/index.html", context)
