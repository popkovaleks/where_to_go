import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загрузка нового места из json'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Адрес json файла')

    def handle(self, *args, **kwargs):
        address = kwargs['link']
        response = requests.get(address).json()

        place, created = Place.objects.get_or_create(
            title=response.get('title'),
            description_short=response.get('description_short'),
            description_long=response.get('description_long'),
            lng=response.get('coordinates').get('lng'),
            lat=response.get('coordinates').get('lat')
        )

        for i, img_link in enumerate(response.get('imgs'), start=1):

            resp_img = requests.get(img_link)
            img, created = Image.objects.get_or_create(
                place=place,
                order_num=i
            )

            content_file = ContentFile(resp_img.content)
            img.image.save(
                img_link.split('/')[-1],
                content_file,
                save=True
            )
