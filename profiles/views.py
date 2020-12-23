from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from checkout.models import Reservation


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    favorites = user.favorite.all()
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
        'favorites': favorites,
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


def reservation_confirmation(request, reservation_number):
    reservation = get_object_or_404(Reservation,
                                    reservation_number=reservation_number)

    messages.info(request, f'This is a past confirmation for reservation \
         number {reservation_number}. \
             A confirmation email was sent on the reservation date')

    template = 'checkout/checkout_success.html'
    context = {
        'reservation': reservation,
        'from_profile': True,
    }
    return render(request, template, context)
