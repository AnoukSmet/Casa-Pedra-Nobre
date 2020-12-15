from django.shortcuts import render

# Create your views here.


def reservation(request):
    template = 'reservation/reservation.html'
    return render(request, template)
