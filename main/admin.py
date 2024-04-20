from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'teaser')
    list_editable = ('title', 'teaser')
    search_fields = ('title', 'teaser')
    ordering = ('-date',)
    list_per_page = 50

