from django.urls import path
from . import views

urlpatterns = [
    path("isitchristmas/", views.is_christmas, name="is_christmas"),
]
