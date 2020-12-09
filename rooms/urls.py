from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_rooms, name="view_rooms"),
]
