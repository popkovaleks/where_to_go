from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('places/<int:place_id>/', views.get_detail_data, name='detail_data'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
