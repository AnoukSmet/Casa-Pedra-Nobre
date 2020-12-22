from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    reservations = profile.reservations.all()
    template = 'profiles/profile.html'
    context = {
        "profile": profile,
        "reservations": reservations,
    }

    return render(request, template, context)


def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, "Profile updated succesfully")
            return redirect('profile')
        else:
            messages.error(request, "Updated failed. \
                Please ensure the form is valid")
    else:
        profile_form = UserProfileForm(instance=profile)
    template = 'profiles/edit_profile.html'
    context = {
        'form': profile_form,
    }
    return render(request, template, context)
