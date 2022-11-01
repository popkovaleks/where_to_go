from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)

    description_short = HTMLField(blank=True, null=True)

    description_long = HTMLField(blank=True, null=True)

    lng = models.FloatField()

    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):

    order_num = models.IntegerField(default=1)

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')

    image = models.ImageField()

    class Meta:
        ordering = ['order_num', ]

    def __str__(self):
        return f'{self.order_num} {self.image.name}'
