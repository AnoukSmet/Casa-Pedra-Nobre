from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from datetime import datetime, timedelta
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


@login_required
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


@login_required
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


@login_required
def view_reservations(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have access to this \
            part of the site.")
        return redirect(reverse('home'))

    reservations = Reservation.objects.all()
    past_reservations = []
    upcoming_reservations = []
    arrivals_today = []
    arrivals_next = []
    departures = []
    inhouse_guests = []
    for reservation in reservations:
        for item in reservation.lineitems.all():
            if item.check_in and item.check_out < datetime.today().date():
                if reservation not in past_reservations:
                    past_reservations.append(reservation)
            elif item.check_in > datetime.today().date():
                if reservation not in upcoming_reservations:
                    upcoming_reservations.append(reservation)

    for reservation in reservations:
        for item in reservation.lineitems.all():
            if item.check_in == datetime.today().date():
                if reservation not in arrivals_today:
                    arrivals_today.append(reservation)
            elif item.check_out == datetime.today().date():
                if reservation not in departures:
                    departures.append(reservation)
            elif item.check_in < datetime.today().date() and item.check_out > datetime.today().date():
                if reservation not in inhouse_guests:
                    inhouse_guests.append(reservation)
            elif item.check_in > datetime.today().date() and item.check_in < datetime.today().date() + timedelta(days=7):
                if reservation not in arrivals_next:
                    arrivals_next.append(reservation)

    template = 'profiles/reservations.html'
    context = {
        "reservations": reservations,
        "past_reservations": past_reservations,
        "upcoming_reservations": upcoming_reservations,
        "arrivals_today": arrivals_today,
        "arrivals_next": arrivals_next,
        "departures": departures,
        "inhouse_guests": inhouse_guests,
    }

    return render(request, template, context)
