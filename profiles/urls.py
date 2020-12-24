from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('reservation_confirmation/<reservation_number>/',
         views.reservation_confirmation, name='reservation_confirmation'),
    path('reservations/', views.view_reservations, name="view_reservations"),
]
