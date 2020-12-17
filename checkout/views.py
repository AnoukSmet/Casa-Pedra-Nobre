from django.shortcuts import render, redirect, reverse, get_object_or_404
from reservation.contexts import reservation_item
from .forms import ReservationForm
from django.contrib import messages
from rooms.models import Room
from .models import ReservationLineItem, Reservation
from datetime import datetime
from django.conf import settings
import stripe


# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        reservation_items = reservation_item(request)
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'comment': request.POST['comment'],
            'eta': request.POST['eta'],
        }
        reservation_form = ReservationForm(form_data)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation_form.save()
            for room in reservation_items["selected_rooms"]:
                selected_room = Room.objects.get(name=room["room"])
                number_of_guests = room["number_of_guests"]
                reservation_request = request.session.get(
                    'reservation_request', {})
                check_in = datetime.strptime(
                    reservation_request["check_in"], '%Y-%m-%d').date()
                check_out = datetime.strptime(
                    reservation_request["check_out"], '%Y-%m-%d').date()

                reservation_line_item = ReservationLineItem(
                        reservation=reservation,
                        room=selected_room,
                        number_of_guests=number_of_guests,
                        check_in=check_in,
                        check_out=check_out,
                    )
                reservation_line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[
                reservation.reservation_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        reservation_form = ReservationForm()
        reservation_items = reservation_item(request)
        reservation_total = reservation_items["reservation_total"]
        rooms = reservation_items["selected_rooms"]
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


def checkout_success(request, reservation_number):
    save_info = request.session.get('save_info')
    reservation = get_object_or_404(
        Reservation, reservation_number=reservation_number)

    messages.success(request, f'Reservation successfully processed! \
        Your reservation number is {reservation_number}. A confirmation \
        email will be sent to {reservation.email}.')

    template = "checkout/checkout_success.html"
    context = {
        "reservation": reservation,
    }

    return render(request, template, context)
