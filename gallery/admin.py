from django.contrib import admin
from .models import GalleryCategory, GalleryImage
# Register your models here.


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'image',
    )


class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
