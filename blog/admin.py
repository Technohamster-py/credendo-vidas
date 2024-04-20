from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title', 'author']
    list_filter = ['author', 'is_published']
    ordering = ['date']
    list_per_page = 20
    readonly_fields = ['preview_cover']
    fields = ['title',
              'cover',
              'preview_cover',
              'summary',
              #'author',
              'body',
              'is_published']
    form = PostAdminForm

    def preview_cover(self, obj):
        cover_url = obj.cover.url
        return mark_safe(f"<img src='{cover_url}' style='max-height: 200px;'>")

