from django.shortcuts import render
from reservation.contexts import reservation_item
from .forms import ReservationForm
from django.contrib import messages


from django.conf import settings

import stripe


# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    reservation_form = ReservationForm()
    reservation_total = 0
    reservation_items = reservation_item(request)
    rooms = reservation_items["selected_rooms"]
    for room in rooms:
        reservation_total += room["room"].price * reservation_items[
            "number_of_nights"]

    stripe_total = round(reservation_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing.  \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'reservation_form': reservation_form,
        'rooms': rooms,
        'reservation_items': reservation_items,
        'reservation_total': reservation_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
     }
    return render(request, template, context)
