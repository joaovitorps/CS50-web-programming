from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger


# Create your views here.
def index(request):
    context = {"flights": Flight.objects.all()}
    return render(request, "flights/index.html", context)


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    }
    return render(request, "flights/flight.html", context)


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["selected_passengers"]))
        passenger.flights.add(flight)

    url = reverse("flights:flight", kwargs={"flight_id": flight_id})

    return HttpResponseRedirect(url)


def passengers(request):
    passengers = Passenger.objects.all()

    context = {"passengers": passengers}

    return render(request, "flights/passengers.html", context)


def passenger(request, passenger_id):
    passenger = Passenger.objects.get(pk=passenger_id)

    context = {"passenger": passenger}
    return render(request, "flights/passenger.html", context)
