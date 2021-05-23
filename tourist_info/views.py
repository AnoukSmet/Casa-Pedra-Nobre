from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Recommendation, RecommendationCategory
from .forms import RecommendationForm
from django.contrib import messages
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
    is_favorite = False
    if recommendation.favorite.filter(id=request.user.id).exists():
        is_favorite = True
    template = 'tourist_info/recommendation_detail.html'
    context = {
        'recommendation': recommendation,
        'is_favorite': is_favorite,
    }

    return render(request, template, context)


def add_to_favorites(request, recommendation_id):
    recommendation = get_object_or_404(Recommendation, id=recommendation_id)
    if recommendation.favorite.filter(id=request.user.id).exists():
        recommendation.favorite.remove(request.user)
        messages.success(request, f'{recommendation} has been successfully \
            removed from your favorites')
    else:
        recommendation.favorite.add(request.user)
        messages.success(request, f'{recommendation} has been successfully \
        added to your favorites')
    return HttpResponseRedirect(reverse(
        'recommendation_detail', kwargs={
            'recommendation_id': recommendation_id}))


def add_recommendation(request):
    form = RecommendationForm()
    template = 'tourist_info/add_recommendation.html'

    context = {
        'form': form
    }
    return render(request, template, context)
