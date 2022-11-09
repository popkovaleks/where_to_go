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

        if response.ok:
            response = response.json()
            try:
                place, created = Place.objects.get_or_create(
                    title=response['title'],
                    defaults={
                        'description_short': response.get('description_short', ''),
                        'description_long': response.get('description_long', ''),
                        'lng': response['coordinates']['lng'],
                        'lat': response['coordinates']['lat']
                        }
                )
            except KeyError:
                print('Title or coordinates was not set')
                return

            if created:
                for i, img_link in enumerate(response.get('imgs', []), start=1):

                    resp_img = requests.get(img_link)
                    if resp_img.ok:
                        Image.objects.get_or_create(
                            place=place,
                            order_num=i,
                            image=ContentFile(resp_img.content,
                                              name=img_link.split('/')[-1])
                        )
                    else:
                        print(f'{i} {img_link} \
                              status: {resp_img.status_code} {resp_img.text}')
        else:
            print(f'status: {response.status_code}, text: {response.text}')
