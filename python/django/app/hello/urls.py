from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("john", views.john, name="john"),
    path("<str:name>", views.greet, name="greet"),
    path("user/<int:id>", views.user, name="user"),
    path("greet/greet1/<str:name>", views.greet1, name="greet1"),
]
