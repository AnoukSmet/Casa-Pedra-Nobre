from django.shortcuts import render, get_object_or_404
from .models import Room, AmenityCategory, Amenity

# Create your views here.


def rooms(request):
    rooms = Room.objects.all()
    categories = AmenityCategory.objects.all()
    amenities = Amenity.objects.all()
    template = 'rooms/rooms.html'
    context = {
        'rooms': rooms,
        'categories': categories,
        'amenities': amenities,
    }
    return render(request, template, context)


def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    template = 'rooms/room_detail.html'
    context = {
        'room': room,
    }
    return render(request, template, context)
