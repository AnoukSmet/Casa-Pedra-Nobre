from django.shortcuts import render
from reservation.contexts import reservation_item
from rooms.models import Room
from .forms import ReservationForm

# Create your views here.


def checkout(request):
    reservation_form = ReservationForm()
    reservation_total = 0
    reservation_items = reservation_item(request)
    rooms = reservation_items["selected_rooms"]
    for room in rooms:
        reservation_total += room["room"].price * reservation_items["number_of_nights"]

    template = 'checkout/checkout.html'
    context = {
        'reservation_form': reservation_form,
        'rooms': rooms,
        'reservation_items': reservation_items,
        'reservation_total': reservation_total,
        'stripe_public_key': 'pk_test_51Hk4KHKGfxT2cXnIH7FZfZRXkABR63JwpC0MX0l7K8lNNymOnosp4kSkgCRRj6bXJIiXoFOUUWPhjr470aC5b11000V6hyOjJp',
        'client_secret': 'test client secret',
     }
    return render(request, template, context)
