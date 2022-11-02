from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place


def index(request):
    query = Place.objects.all()
    features = []
    for item in query:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [item.lng, item.lat]
            },
            'properties': {
                'title': item.title,
                'detailsUrl': f'places/{item.pk}'
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


def detail_data(request, id):
    obj = get_object_or_404(Place, pk=id)
    data = {
        'title': obj.title,
        'imgs': [img.image.url for img in obj.images.all()],
        'description_short': obj.description_short,
        'description_long': obj.description_long,
        'coordinates': {
            'lat': obj.lat,
            'lng': obj.lng
        }
    }
    return JsonResponse(data)
