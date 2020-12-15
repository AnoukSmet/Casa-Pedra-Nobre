from django.contrib import admin
from .models import Reservation, ReservationLineItem
# Register your models here.


class ReservationLineItemAdminInline(admin.TabularInline):
    model = ReservationLineItem
    readonly_fields = ('lineitem_total', 'number_of_nights')


class ReservationAdmin(admin.ModelAdmin):
    inlines = (ReservationLineItemAdminInline,)
    readonly_fields = ('reservation_number', 'reservation_total',
                       'date',)

    fields = ('reservation_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'reservation_total', 'eta', 'comment')

    list_display = ('reservation_number', 'full_name',
                    'reservation_total',)

    ordering = ('-reservation_number',)


admin.site.register(Reservation, ReservationAdmin)
