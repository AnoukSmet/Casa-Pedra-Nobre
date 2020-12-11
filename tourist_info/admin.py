from django.contrib import admin
from .models import Recommendation, RecommendationCategory
# Register your models here.


class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'intro',
        'category',
    )

    ordering = ('category',)


class RecommendationCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(RecommendationCategory, RecommendationCategoryAdmin)
