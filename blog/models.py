from django.db import models
from cuser.fields import CurrentUserField


class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('Заголовок', max_length=50)
    body = models.TextField('Тело статьи')
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    #date_published = models.DateTimeField('Дата публикации', blank=True, null=True)
    author = CurrentUserField(related_name='post_author', add_only=True, on_delete=models.CASCADE, verbose_name='Автор')
    cover = models.ImageField('Обложка', blank=True)
    summary = models.CharField('Краткое описание', max_length=200, blank=True)
    is_published = models.BooleanField('Опубликовать', default=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

# Create your models here.
