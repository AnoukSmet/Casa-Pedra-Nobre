from django.http import HttpResponse
from rooms.models import Room
from .models import Reservation, ReservationLineItem
import json
import time
from datetime import datetime


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        reservation_request = intent.metadata.reservation_request
        test123 = intent.metadata.test123
        save_info = intent.metadata.save_info
        
        billing_details = intent.charges.data[0].billing_details
        reservation_total = round(intent.charges.data[0].amount / 100, 2)

        reservation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                reservation = Reservation.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    reservation_total=reservation_total,
                    original_reservation=reservation_request,
                    stripe_pid=pid,
                )
                reservation_exists = True
                break
            except Reservation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if reservation_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            reservation = None
            try:
                reservation = Reservation.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    reservation_total=reservation_total,
                    original_reservation=reservation_request,
                    stripe_pid=pid
                )
                test123 = json.loads(test123)
                for key, value in test123.items():
                    room = Room.objects.get(pk=key)
                    number_of_guests = value
                    reservation_request = json.loads(reservation_request)
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
            except Exception as e:
                if reservation:
                    reservation.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                            status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created reservation in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
