from django.db import models
from django.db import transaction

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    max_number_of_guests = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.name


class Image(models.Model):
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name="images")
    image = models.ImageField()
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.room.name

    def save(self, *args, **kwargs):
        if not self.main_image:
            return super(Image, self).save(*args, **kwargs)
        with transaction.atomic():
            Image.objects.filter(room__id=self.room.id,
                                 main_image=True).update(main_image=False)
            return super(Image, self).save(*args, **kwargs)


class AmenityCategory(models.Model):
    class Meta:
        verbose_name_plural = 'AmenityCategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    class Meta:
        verbose_name_plural = 'Amenities'

    category = models.ForeignKey('AmenityCategory',
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
