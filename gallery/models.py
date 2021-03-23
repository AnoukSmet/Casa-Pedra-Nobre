from django.db import models

# Create your models here.


class GalleryCategory(models.Model):
    class Meta:
        verbose_name_plural = 'GalleryCategories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    category = models.ForeignKey('GalleryCategory',
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    image = models.ImageField()

    def __str__(self):
        return self.category.name