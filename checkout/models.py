import uuid
from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from rooms.models import Room
from profiles.models import UserProfile
from datetime import datetime
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    reservation_number = models.CharField(
        max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="reservations")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    reservation_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    comment = models.TextField(null=True, blank=True)
    eta = models.CharField(max_length=254, null=True, blank=True)
    original_reservation = models.TextField(
        null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=True, blank=True, default='')

    def _generate_reservation_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.reservation_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.reservation_number:
            self.reservation_number = self._generate_reservation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation_number


class ReservationLineItem(models.Model):
    reservation = models.ForeignKey(
        Reservation, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    room = models.ForeignKey(
        Room, null=False, blank=False, on_delete=models.CASCADE)
    number_of_guests = models.IntegerField(null=False, blank=False, default=2)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_nights = models.IntegerField(null=False, blank=False)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)
    
    def _calculate_number_of_nights(self):
        check_in = self.check_in
        check_out = self.check_out
        delta = check_out - check_in
        self.number_of_nights = delta.days

    def save(self, *args, **kwargs):
        self._calculate_number_of_nights()
        self.lineitem_total = self.number_of_nights * self.room.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation.reservation_number
