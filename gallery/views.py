from django.shortcuts import render
from rooms.models import Image
from tourist_info.models import Recommendation


# Create your views here.


def gallery(request):
    template = "gallery/gallery.html"
    
    images_cpn = Image.objects.all()

    recommendations = Recommendation.objects.all()
    images_surroundings = []
    for recommendation in recommendations:
        images_surroundings.append(recommendation.image)

    context = {
        'images_cpn': images_cpn,
        'images_surroundings': images_surroundings,
    }
    return render(request, template, context)
