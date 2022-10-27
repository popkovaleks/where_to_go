from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

    fields = ['image', 'image_preview', 'order_num']
    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        return mark_safe("<img src=\"{url}\" height={height})>".format(
            url=obj.image.url,
            height=200
        ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_short')
    list_display_links = ('title_short',)

    inlines = [ImageInline,]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass