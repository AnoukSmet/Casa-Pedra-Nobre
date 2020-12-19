from datetime import datetime
from rooms.models import Room
import json


def reservation_item(request):
    check_in = ""
    check_out = ""
    number_of_nights = 0
    reservation_total = 0

    test123 = request.session.get('test123', {})

    reservation_request = request.session.get('reservation_request', {})
    if reservation_request != {}:
        check_in = datetime.strptime(
            reservation_request["check_in"], '%Y-%m-%d').date()
        check_out = datetime.strptime(
            reservation_request["check_out"], '%Y-%m-%d').date()
        number_of_nights = (check_out - check_in).days

    for key in test123.keys():
        room = Room.objects.get(pk=key)
        reservation_total += room.price * number_of_nights

    context = {
        'check_in': check_in,
        'check_out': check_out,
        'number_of_nights': number_of_nights,
        'reservation_total': reservation_total,
    }

    return context
