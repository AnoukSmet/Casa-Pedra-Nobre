from datetime import datetime
from rooms.models import Room


def reservation_item(request):
    check_in = ""
    check_out = ""
    number_of_nights = 0
    reservation_total = 0
    reservation_request = request.session.get('reservation_request', {})

    check_in = datetime.strptime(
            reservation_request["check_in"], '%Y-%m-%d').date()
    check_out = datetime.strptime(
            reservation_request["check_out"], '%Y-%m-%d').date()
    number_of_nights = (check_out - check_in).days

    rooms = request.session["selected_rooms"]["rooms"]
    number_of_guests = request.session["selected_rooms"]["number_of_guests"]
    rooms_checkbox = request.session["selected_rooms"]["rooms_checkbox"]

    selected_rooms = []

    i = 0
    while i < len(rooms):
        for item in rooms_checkbox:
            if item in rooms:
                room = Room.objects.get(pk=item)
                selected_rooms.append({
                    "room": room,
                    "number_of_guests": number_of_guests[i],
                    "room_total": room.price * number_of_nights,
                })
        i += 1

    cleaned_selected_rooms = []
    for i in range(0, len(selected_rooms)):
        if selected_rooms[i] not in cleaned_selected_rooms:
            cleaned_selected_rooms.append(selected_rooms[i])

    for room in cleaned_selected_rooms:
        reservation_total += room["room"].price * number_of_nights

    context = {
        'check_in': check_in,
        'check_out': check_out,
        'number_of_nights': number_of_nights,
        'selected_rooms': cleaned_selected_rooms,
        'reservation_total': reservation_total,
    }

    return context
