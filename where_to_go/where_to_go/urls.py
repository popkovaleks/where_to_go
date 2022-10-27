from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('places/<int:id>', views.detail_data, name='detail_data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
