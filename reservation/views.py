from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from rooms.models import Room
from datetime import datetime
from django.contrib import messages
from checkout.models import ReservationLineItem
# Create your views here.


def reservation(request):
    rooms = Room.objects.all()
    error = ""
    unavailable_rooms = []
    available_rooms = []
    print(type(unavailable_rooms))
    if request.method == 'POST':
        form = {
            'check_in': request.POST.get('check_in'),
            'check_out': request.POST.get('check_out'),
        }
        check_in = datetime.strptime(
                            form["check_in"], '%Y-%m-%d').date()
        check_out = datetime.strptime(form["check_out"], '%Y-%m-%d').date()
        if check_in >= datetime.today().date():
            if check_out >= check_in:
                for room in rooms:
                    reservations = ReservationLineItem.objects.filter(
                        room__id=room.id)
                    if reservations:
                        for reservation in reservations:
                            if check_availability(
                                    reservation.check_in,
                                    reservation.check_out,
                                    check_in,
                                    check_out):
                                unavailable_rooms.append(room.id)
                                print(room.id)
                            else:
                                available_rooms.append(room.id)
                                print(room.id)
                    else:
                        available_rooms.append(room.id)
                        print(room.id)
            else:
                messages.error(request, 'Your check in date can not be in the past. \
                    Please select another date.')
                return redirect(reverse('reservation'))
        else:
            messages.error(request, 'Your check out date needs to be after the check in date.\
                 Please select another date.')
            return redirect(reverse('reservation'))
        i = 0
        while i < len(rooms):
            for available_room in available_rooms:
                if available_room in unavailable_rooms:
                    available_rooms.remove(available_room)
            i += 1
        available_rooms = list(dict.fromkeys(available_rooms))
        request.session['reservation_request'] = form
        request.session['available_rooms'] = available_rooms
        request.session['unavailable_rooms'] = unavailable_rooms

        return HttpResponseRedirect(reverse('reservation_detail'))
    else:
        context = {
            'rooms': rooms,
            'error': error,
        }

        return render(request, 'reservation/reservation.html', context)


def check_availability(
        check_in, check_out, check_in_request, check_out_request):
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
    template = "reservation/reservation_detail.html"
    form = request.session['reservation_request']
    check_in = form["check_in"]
    check_out = form["check_out"]
    available_rooms = request.session["available_rooms"]
    unavailable_rooms = request.session["unavailable_rooms"]

    context = {
        'check_in': check_in,
        'check_out': check_out,
        'available_rooms': available_rooms,
        'unavailable_rooms': unavailable_rooms,
    }
    return render(request, template, context)
