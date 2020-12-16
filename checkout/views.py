from django.shortcuts import render
from reservation.contexts import reservation_item
from rooms.models import Room

# Create your views here.


def checkout(request):
    reservation_total = 0
    reservation_items = reservation_item(request)
    rooms = reservation_items["selected_rooms"]
    for room in rooms:
        reservation_total += room["room"].price * reservation_items["number_of_nights"]

    template = 'checkout/checkout.html'
    context = {
        'rooms': rooms,
        'reservation_items': reservation_items,
        'reservation_total': reservation_total,
     }
    return render(request, template, context)
