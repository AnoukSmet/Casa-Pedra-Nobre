from datetime import datetime
from rooms.models import Room


def reservation_item(request):
    check_in = ""
    check_out = ""
    number_of_nights = 0
    order_total = 0
    reservation_request = request.session.get('reservation_request', {})

    check_in = datetime.strptime(
            reservation_request["check_in"], '%Y-%m-%d').date()
    check_out = datetime.strptime(
            reservation_request["check_out"], '%Y-%m-%d').date()
    number_of_nights = (check_out - check_in).days

    rooms = Room.objects.all()
    number_of_people = request.session["selected_rooms"]["number_of_guests"]
    rooms_checkbox = request.session["selected_rooms"]["rooms_checkbox"]
    
    context = {
        'check_in': check_in,
        'check_out': check_out,
        'number_of_nights': number_of_nights,
        'rooms_checkbox': rooms_checkbox,
    }

    return context
