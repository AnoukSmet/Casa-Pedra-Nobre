from django.shortcuts import render, get_object_or_404
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


def recommendation_detail(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, pk=recommendation_id)

    template = 'tourist_info/recommendation_detail.html'
    context = {
        'recommendation': recommendation,
    }

    return render(request, template, context)
