from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'detailsUrl': reverse('detail_data', args=(place.pk, ))
            }
        }
        features.append(feature)

    geo_data = {
        'geo_data': {
            'type': 'FeatureCollection',
            'features': features
        }
    }

    return render(request, 'index.html', geo_data)


def get_detail_data(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_info = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(place_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})
