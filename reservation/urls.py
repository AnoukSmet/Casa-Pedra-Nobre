from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name="reservation"),
    path('reservation_detail', views.reservation_detail, name="reservation_detail"),
]
