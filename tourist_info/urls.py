from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourist_info, name="tourist_info"),
]
