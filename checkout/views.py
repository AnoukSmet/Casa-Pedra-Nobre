from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST

from reservation.contexts import reservation_item
from .forms import ReservationForm
from django.contrib import messages
from rooms.models import Room
from .models import ReservationLineItem, Reservation
from datetime import datetime
from django.conf import settings
import stripe
import json


# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'reservation_request': json.dumps(
                request.session.get('reservation_request', {})),
            'test123': json.dumps(
                request.session.get('test123', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        reservation_items = reservation_item(request)
        reservation_request = request.session.get('reservation_request', {})
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
            pid = request.POST.get('client_secret').split('_secret')[0]
            reservation.stripe_pid = pid
            reservation.original_reservation = json.dumps(reservation_request)
            reservation.reservation_total = reservation_items[
                "reservation_total"]
            reservation.save()

            test123 = request.session.get('test123', {})
            for key, value in test123.items():
                room = Room.objects.get(pk=key)
                number_of_guests = value
                reservation_request = request.session.get(
                    'reservation_request', {})
                check_in = datetime.strptime(
                    reservation_request["check_in"], '%Y-%m-%d').date()
                check_out = datetime.strptime(
                    reservation_request["check_out"], '%Y-%m-%d').date()
                number_of_nights = (check_out - check_in).days
                reservation_line_item = ReservationLineItem(
                    reservation=reservation,
                    room=room,
                    number_of_guests=number_of_guests,
                    check_in=check_in,
                    check_out=check_out,
                    number_of_nights=number_of_nights,
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
        test123 = request.session.get('test123', {})
        rooms = []
        for key in test123.keys():
            room = Room.objects.get(pk=key)
            rooms.append(room)

        reservation_total = reservation_items["reservation_total"]
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
