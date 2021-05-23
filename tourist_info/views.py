from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import Recommendation, RecommendationCategory
from .forms import RecommendationForm
from django.contrib.auth.decorators import login_required
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


@login_required
def add_recommendation(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only property admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save()
            messages.success(request, "Successfully added recommendation")
            return redirect(reverse('recommendation_detail', args=[recommendation.id]))
        else:
            messages.error(request, "Failed to add recommendation. \
            Please ensure the form is valid.")
    else:
        form = RecommendationForm()
        template = 'tourist_info/add_recommendation.html'

        context = {
            'form': form
        }
        return render(request, template, context)


@login_required
def edit_recommendation(request, recommendation_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only property admins can do that.')
        return redirect(reverse('home'))
    
    recommendation = get_object_or_404(Recommendation, pk=recommendation_id)

    if request.method == "POST":
        form = RecommendationForm(request.POST, request.FILES,
                                  instance=recommendation)
        if form.is_valid:
            form.save()
            messages.info(request, 'You have successfully updated \
                recommendation.')
            return redirect(reverse('recommendation_detail',
                            args=[recommendation.id]))

        else:
            messages.error(request, 'Failed to update recommendation. \
            Please ensure the form is valid.')
    form = RecommendationForm(instance=recommendation)
    messages.info(request, f'You are editing recommendation: \
         {recommendation.name}')
    template = 'tourist_info/edit_recommendation.html'

    context = {
        'form': form,
        'recommendation': recommendation
    }
    return render(request, template, context)


@login_required
def delete_recommendation(request, recommendation_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only property admins can do that.')
        return redirect(reverse('home'))

    recommendation = get_object_or_404(Recommendation, pk=recommendation_id)
    recommendation.delete()
    messages.success(request, 'Recommendation successfully deleted')
    return redirect(reverse('tourist_info'))
