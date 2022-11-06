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
        response = requests.get(address)

        if response.status_code != 200:
            print(f'status: {response.status_code}, text: {response.text}')
            return
        
        response = response.json()
        place, created = Place.objects.get_or_create(
            title=response.get('title', 'Введите название!'),
            defaults={'description_short': response.get('description_short', ''),
                       'description_long': response.get('description_long', ''),
                       'lng': response.get('coordinates').get('lng'),
                       'lat': response.get('coordinates').get('lat')}
        )
        print(created)
        if created and response.get('imgs'):
            for i, img_link in enumerate(response.get('imgs'), start=1):

                resp_img = requests.get(img_link)
                img, created_img = Image.objects.get_or_create(
                    place=place,
                    order_num=i
                )

                content_file = ContentFile(resp_img.content)
                img.image.save(
                    img_link.split('/')[-1],
                    content_file,
                    save=True
                )
