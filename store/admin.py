from django.contrib import admin
from .models import Tag, Item, Operation, Color
from django.db.models import QuerySet
from django.utils.safestring import mark_safe


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'preview', 'status', 'last_status_change']
    list_editable = ['status']
    ordering = ['name']
    list_per_page = 10
    filter_horizontal = ['tags', 'color']
    actions = ['set_stored', 'set_active']
    search_fields = ['name']
    list_filter = ['status', 'tags', 'color']
    readonly_fields = ['preview']
    fields = ['name', 'photo', 'preview', 'place', 'size', 'material', 'color', 'status', 'last_status_change', 'tags']


    def preview(self, obj):
        photo_url = obj.photo.url
        return mark_safe(f"<img src='{photo_url}' style='max-height: 200px;'>")

    @admin.action(description='Отметить сданными')
    def set_stored(self, request, qs: QuerySet):
        qs.update(status=Item.STORED)

    @admin.action(description='Отметить активными')
    def set_active(self, request, qs: QuerySet):
        qs.update(status=Item.ACTIVE)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_editable = ['title']
    ordering = ['title']
    search_fields = ['title']


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['date', 'last_name', 'action', 'item']
    ordering = ['date']
    list_filter = ['action', 'last_name']
    search_fields = ['item']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'color']
    list_editable = ['color']