from enum import unique
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)

    title_short = models.CharField(max_length=200, null=True)

    placeId = models.CharField(max_length=200, null=True, blank=True)

    description_short = HTMLField()

    description_long = HTMLField()

    lng = models.FloatField()

    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=200)

    order_num = models.IntegerField(default=1)

    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1, related_name='images')

    image = models.ImageField()

    class Meta:
        ordering = ['order_num',]

    def __str__(self):
        return f'{self.order_num} {self.name}'