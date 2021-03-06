from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from rooms.models import Room
from datetime import datetime
from django.contrib import messages
from checkout.models import ReservationLineItem
# Create your views here.


def reservation(request):
    rooms = Room.objects.all()
    unavailable_rooms = []
    available_rooms = []
    if request.method == 'POST':
        form = {
            'check_in': request.POST.get('check_in'),
            'check_out': request.POST.get('check_out'),
        }
        # Checks if users filled in check-in and check-out
        if form["check_in"] and form["check_out"]:
            check_in = datetime.strptime(
                                form["check_in"], '%Y-%m-%d').date()
            check_out = datetime.strptime(form["check_out"], '%Y-%m-%d').date()
            # checks if reservation is not for longer than 28 days
            if (check_out - check_in).days > 28:
                messages.error(request, 'It is not possible to make a reservation online for more than 28 days. \
                    Please contact us by phone or email if you wish to \
                        stay longer than 28 days.')
                return redirect(reverse('reservation'))
            else:
                # checks if check-in is equal or later than today
                if check_in >= datetime.today().date():
                    # checks that check-out is after check-in
                    if check_out > check_in:
                        for room in rooms:
                            reservations = ReservationLineItem.objects.filter(
                                room__id=room.id)
                            if reservations:
                                # Compares reservation request to each reservation
                                # to check for overlap
                                for reservation in reservations:
                                    if check_availability(
                                            reservation.check_in,
                                            reservation.check_out,
                                            check_in,
                                            check_out):
                                        unavailable_rooms.append(room.id)
                                    else:
                                        available_rooms.append(room.id)
                            else:
                                available_rooms.append(room.id)
                    else:
                        messages.error(request, 'Your check out date needs to be after the check in date.\
                        Please select another date.')
                        return redirect(reverse('reservation'))
                else:
                    messages.error(request, 'Your check in date can not be in the past. \
                            Please select another date.')
                    return redirect(reverse('reservation'))
        else:
            messages.error(request, 'Please select a check-in date and a check-out date \
                 in order to view prices and availability')
            return redirect(reverse('reservation'))

        # Removes dupplicates
        new_available_rooms = list(dict.fromkeys(available_rooms))
        new_unavailable_rooms = list(dict.fromkeys(unavailable_rooms))

    

        # when rooms is already in unavailable rooms,
        # remove from available rooms
        i = 0
        while i <= len(new_available_rooms):
            for available_room in new_available_rooms:
                if available_room in new_unavailable_rooms:
                    new_available_rooms.remove(available_room)
            i = i + 1
    

        request.session['reservation_request'] = form
        request.session['available_rooms'] = new_available_rooms
        request.session['unavailable_rooms'] = new_unavailable_rooms

        return HttpResponseRedirect(reverse('reservation_detail'))
    else:
        return render(request, 'reservation/reservation.html')

# Credits to Alexandre Pinto for the check availability logic which I adjusted for my situation
# https://github.com/alexpnt/django-calendar/blob/master/events/models.py
def check_availability(
        check_in, check_out, check_in_request, check_out_request):
    """
    Checks overlap with requested check-in and check-out
    Compared to existing reservations
    """
    overlap = False
    if check_in_request == check_out or check_out_request == check_in:
        overlap = False
    elif (check_in_request >= check_in and check_in_request <= check_out) or (
          check_out_request >= check_in and check_out_request <= check_out):
        overlap = True
    elif check_in_request <= check_in and check_out_request >= check_out:
        overlap = True

    return overlap


def reservation_detail(request):
    if request.method == "POST":
        reservation_request = request.session["reservation_request"]
        check_in = datetime.strptime(
            reservation_request["check_in"], '%Y-%m-%d').date()
        check_out = datetime.strptime(
            reservation_request["check_out"], '%Y-%m-%d').date()
        number_of_nights = (check_out - check_in).days
        data = request.POST
        # Checks if user has selected at least 1 room
        if 'select-room' in data:
            rooms = []
            number_of_guests = []
            selected_rooms = []
            merged_reservation_data = {}
            room_request = {}
            # Stores key value pairs with room id and number of guests
            for key, value in data.lists():
                if key == "room_id":
                    for v in value:
                        rooms.append(v)
                elif key == "number_of_guests":
                    for v in value:
                        number_of_guests.append(v)
                elif key == "select-room":
                    for v in value:
                        selected_rooms.append(v)
            i = 0
            while i < len(rooms):
                merged_reservation_data[rooms[i]] = number_of_guests[i]
                i += 1

            for k, v in merged_reservation_data.items():
                for room in selected_rooms:
                    if room == k:
                        room_request[k] = v

            request.session['room_request'] = room_request

            return redirect('checkout')
        else:
            messages.error(request, 'You need to select at least 1 room \
                in order to proceed.')
            return redirect(reverse('reservation_detail'))
    else:
        # Displays available and unavailable rooms
        form = request.session['reservation_request']
        check_in = datetime.strptime(form["check_in"], '%Y-%m-%d').date()
        check_out = datetime.strptime(form["check_out"], '%Y-%m-%d').date()
        available_rooms = request.session["available_rooms"]
        unavailable_rooms = request.session["unavailable_rooms"]
        available_room = []
        unavailable_room = []
        number_of_nights = (check_out - check_in).days
        for room in available_rooms:
            room = Room.objects.get(pk=room)
            available_room.append(room)
        for room in unavailable_rooms:
            room = Room.objects.get(pk=room)
            unavailable_room.append(room)
        template = 'reservation/reservation_detail.html'
        context = {
            'form': form,
            'check_in': form["check_in"],
            'check_out': form["check_out"],
            'available_rooms': available_room,
            'unavailable_rooms': unavailable_room,
            'number_of_nights': number_of_nights,
        }

    return render(request, template, context)
