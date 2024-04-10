from django.shortcuts import render

from .models import Flight


# Create your views here.
def index(request):
    context = {"flights": Flight.objects.all()}
    return render(request, "flights/index.html", context)


def flight(request, id):
    flight = Flight.objects.filter(id=id)

    context = {"flight": flight.get()}
    return render(request, "flights/flight.html", context)
