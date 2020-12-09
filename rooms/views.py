from django.shortcuts import render
from .models import Room

# Create your views here.


def rooms(request):
    rooms = Room.objects.all()
    template = 'rooms/rooms.html'
    context = {
        'rooms': rooms
    }
    return render(request, template, context)
