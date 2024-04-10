from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    # flights
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    # passengers
    path("passengers", views.passengers, name="passengers"),
    path("passengers/<int:passenger_id>", views.passenger, name="passenger"),
]
