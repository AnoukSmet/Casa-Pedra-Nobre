from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from datetime import datetime


# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    reservations = profile.reservations.all()
    upcoming_reservations = []
    past_reservations = []
    for reservation in reservations:
        for item in reservation.lineitems.all():
            if item.check_in >= datetime.today().date():
                if reservation not in upcoming_reservations:
                    upcoming_reservations.append(reservation)
            else:
                past_reservations.append(reservation)
    template = 'profiles/profile.html'
    context = {
        "profile": profile,
        "reservations": reservations,
        "upcoming_reservations": upcoming_reservations,
        "past_reservations": past_reservations,
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
