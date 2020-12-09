from django.shortcuts import render

# Create your views here.


def view_rooms(request):
    return render(request, 'rooms/rooms.html')
