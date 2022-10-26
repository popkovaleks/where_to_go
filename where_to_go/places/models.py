from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200)

    description_short = models.TextField()

    description_long = models.TextField()

    lng = models.FloatField()

    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=200)

    order_num = models.IntegerField(default=1)

    image = models.ImageField()

    def __str__(self):
        return f'{self.order_num} {self.name}'