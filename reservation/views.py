from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from rooms.models import Room
from datetime import datetime
from django.contrib import messages
# Create your views here.


def reservation(request):
    rooms = Room.objects.all()
    error = ""
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
                print("Good")
            else:
                messages.error(request, 'Your check in date can not be in the past. \
                    Please select another date.')
                return redirect(reverse('reservation'))
        else:
            messages.error(request, 'Your check out date needs to be after the check in date.\
                 Please select another date.')
            return redirect(reverse('reservation'))

        request.session['reservation_request'] = form
        return HttpResponseRedirect(reverse('reservation_detail'))
    else:
        context = {
            'rooms': rooms,
            'error': error,
        }

        return render(request, 'reservation/reservation.html', context)


def reservation_detail(request):
    template = "reservation/reservation_detail.html"
    return render(request, template)
