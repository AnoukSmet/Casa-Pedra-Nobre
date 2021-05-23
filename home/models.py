from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class PageIntro(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    url_name = models.CharField(max_length=50, null=True, blank=True)
    display_order = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)],
        unique=True)

    def __str__(self):
        return self.title
