from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Заголовок', max_length=200)
    teaser = models.CharField('Сводка', max_length=300, default="Тизер")
    content = models.TextField('Контент', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField('Тип', max_length=20, default='news')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
