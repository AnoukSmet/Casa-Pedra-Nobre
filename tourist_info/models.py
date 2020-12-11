from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class RecommendationCategory(models.Model):
    class Meta:
        verbose_name_plural = 'RecommendationCategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    category = models.ForeignKey('RecommendationCategory',
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    image = models.ImageField()
    intro = models.TextField()
    description = models.TextField()
    link_to_website = models.URLField()
    link_to_google_maps = models.URLField(max_length=500)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    favorite = models.ManyToManyField(
        User, related_name='favorite', blank=True)

    def __str__(self):
        return self.name
