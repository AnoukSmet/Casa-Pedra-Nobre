from django.shortcuts import render

# Create your views here.


def gallery(request):
    template = "gallery/gallery.html"

    return render(request, template)
