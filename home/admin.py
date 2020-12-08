from django.contrib import admin
from .models import PageIntro

# Register your models here.


class PageIntroAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image',
        'url_name',
        'display_order',
    )
    ordering = ('display_order',)


admin.site.register(PageIntro, PageIntroAdmin)
