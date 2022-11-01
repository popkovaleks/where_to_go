from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
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
    list_display = ('id', 'title')
    list_display_links = ('title', )
    search_fields = ['title', ]
    inlines = [ImageInline, ]
