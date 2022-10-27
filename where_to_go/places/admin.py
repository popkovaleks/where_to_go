from django.contrib import admin

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_short')
    list_display_links = ('title_short',)

    inlines = [ImageInline,]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass