from django.shortcuts import render
from .models import Recommendation, RecommendationCategory
# Create your views here.


def tourist_info(request):
    recommendations = Recommendation.objects.all()
    categories = RecommendationCategory.objects.all()

    template = 'tourist_info/tourist_info.html'
    context = {
        'recommendations': recommendations,
        'categories': categories,
    }

    return render(request, template, context)
