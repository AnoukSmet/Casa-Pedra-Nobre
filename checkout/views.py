from datetime import datetime
import json
import stripe

from django.shortcuts import render, redirect, reverse,\
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


from reservation.contexts import reservation_item

from rooms.models import Room, Amenity
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from .forms import ReservationForm
from .models import ReservationLineItem, Reservation


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        comment = request.POST.get('comment')
        eta = request.POST.get('eta')
        if len(comment) == 0:
            comment = "N/A"
        if len(eta) == 0:
            eta = "N/A"
        stripe.PaymentIntent.modify(pid, metadata={
            'reservation_request': json.dumps(
                request.session.get('reservation_request', {})),
            'room_request': json.dumps(
                request.session.get('room_request', {})),
            'save_info': request.POST.get('save_info'),
            'comment': comment,
            'eta': eta,
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
    try:
        if request.method == "POST":
            reservation_items = reservation_item(request)
            reservation_request = request.session.get(
                'reservation_request', {})
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
                if not request.user.is_superuser:
                    pid = request.POST.get('client_secret').split('_secret')[0]
                    reservation.stripe_pid = pid
                reservation.original_reservation = json.dumps(
                    reservation_request)
                reservation.reservation_total = reservation_items[
                    "reservation_total"]
                reservation.save()

                room_request = request.session.get('room_request', {})
                for key, value in room_request.items():
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
            room_request = request.session.get('room_request', {})

            rooms = []
            number_of_guests = []
            merged_reservation_data = {}
            for key, value in room_request.items():
                room = Room.objects.get(pk=key)
                rooms.append(room)
                number_of_guests.append(value)
            i = 0
            while i < len(rooms):
                merged_reservation_data[rooms[i]] = number_of_guests[i]
                i += 1

            reservation_total = reservation_items["reservation_total"]
            stripe_total = round(reservation_total * 100)
            stripe.api_key = stripe_secret_key
            if not request.user.is_superuser:
                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )

                if request.user.is_authenticated:
                    try:
                        profile = UserProfile.objects.get(user=request.user)
                        reservation_form = ReservationForm(initial={
                            'full_name': profile.default_full_name,
                            'email': profile.user.email,
                            'phone_number': profile.default_phone_number,
                            'country': profile.default_country
                        })
                    except UserProfile.DoesNotExist:
                        reservation_form = ReservationForm()
                else:
                    reservation_form = ReservationForm()

                if not stripe_public_key:
                    messages.warning(request, 'Stripe Public Key is missing.  \
                        Did you forget to set it in your environment?')
                template = 'checkout/checkout.html'
                context = {
                    'reservation_form': reservation_form,
                    'rooms': merged_reservation_data,
                    'reservation_items': reservation_items,
                    'reservation_total': reservation_total,
                    'stripe_public_key': stripe_public_key,
                    'client_secret': intent.client_secret,
                    }
                return render(request, template, context)

            else:
                template = 'checkout/checkout.html'
                context = {
                    'reservation_form': reservation_form,
                    'rooms': merged_reservation_data,
                    'reservation_items': reservation_items,
                    'reservation_total': reservation_total,
                }
            return render(request, template, context)
    except Exception as e:
        messages.error(request, 'Looks like something went wrong. \
            Our apologies for the inconvenience.')
        return HttpResponse(content=e, status=400)


def checkout_success(request, reservation_number):
    amenities = Amenity.objects.all()
    save_info = request.session.get('save_info')
    reservation = get_object_or_404(
        Reservation, reservation_number=reservation_number)

    if reservation.stripe_pid == '':
        send_confirmation_email(reservation)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        reservation.user_profile = profile
        reservation.save()

    if save_info:
        profile_data = {
            'default_full_name': reservation.full_name,
            'default_email': reservation.email,
            'default_phone_number': reservation.phone_number,
            'default_country': reservation.country
        }

        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Reservation successfully processed! \
        Your reservation number is {reservation_number}. A confirmation \
        email will be sent to {reservation.email}.')

    template = "checkout/checkout_success.html"
    context = {
        "reservation": reservation,
        "amenities": amenities
    }

    return render(request, template, context)


def send_confirmation_email(reservation):
    client_email = reservation.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'reservation': reservation})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'reservation': reservation,
            'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [client_email]
    )
