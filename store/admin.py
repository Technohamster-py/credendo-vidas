import datetime

from django.contrib import admin
from .models import Tag, Item, Operation, Color, Category
from django.db.models import QuerySet
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'parent']
    ordering = ['name']


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
    def save_model(self, request, obj, form, change):
        item = Item.objects.get(name=obj.item)
        item.last_status_change = datetime.datetime.now()

        if obj.action == obj.TAKE:
            item.status = item.ACTIVE
        else:
            item.status = item.STORED

        item.save()
        super().save_model(request, obj, form, change)

    list_display = ['date', 'last_name', 'action', 'item']
    ordering = ['-date']
    list_filter = ['action', 'last_name']
    search_fields = ['item']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'color']
    list_editable = ['color']