from django.contrib import admin
from .models import Room, Image
# Register your models here.


class ImageAdmin(admin.TabularInline):
    model = Image


class RoomAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    list_display = (
        'name',
        'description',
        'price',
        'max_number_of_guests',
    )


admin.site.register(Room, RoomAdmin)
