from django.urls import path
from . import views

urlpatterns = [
    path("isitchristmas/", views.index, name="index"),
]
