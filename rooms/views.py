from django.shortcuts import render
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
