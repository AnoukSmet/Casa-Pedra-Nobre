from django.shortcuts import render
from rooms.models import Image
from .models import GalleryImage
from tourist_info.models import Recommendation


# Create your views here.


def gallery(request):
    template = "gallery/gallery.html"

    images_cpn = []
    images_surroundings = []

    gallery_images = GalleryImage.objects.all()
    for image in gallery_images:
        if str(image.category) == 'cpn':
            images_cpn.append(image)
        elif str(image.category) == 'surroundings':
            images_surroundings.append(image)

    room_images = Image.objects.all()
    for image in room_images:
        images_cpn.append(image)

    recommendations = Recommendation.objects.all()
    for recommendation in recommendations:
        if str(recommendation.category) != 'where_to_eat':
            images_surroundings.append(recommendation)

    context = {
        'images_cpn': images_cpn,
        'images_surroundings': images_surroundings,
    }
    return render(request, template, context)
