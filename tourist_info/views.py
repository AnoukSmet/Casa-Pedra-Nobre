from django.shortcuts import render

# Create your views here.


def tourist_info(request):
    return render(request, 'tourist_info/tourist_info.html')
