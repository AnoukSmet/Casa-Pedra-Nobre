from django.shortcuts import render
from reservation.contexts import reservation_item
from rooms.models import Room

# Create your views here.


def checkout(request):
    reservation_items = reservation_item(request)
    selected_rooms = []
    for room in reservation_items["rooms_checkbox"]:
        room = Room.objects.get(pk=room)
        selected_rooms.append(room)

    template = 'checkout/checkout.html'
    context = {
        'rooms': selected_rooms,
     }
    return render(request, template, context)
