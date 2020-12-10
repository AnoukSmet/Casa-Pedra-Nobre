from django.contrib import admin
from .models import Room, Image, AmenityCategory, Amenity
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


class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
    )


class AmenityCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Amenity, AmenityAdmin)
admin.site.register(AmenityCategory, AmenityCategoryAdmin)
admin.site.register(Room, RoomAdmin)
