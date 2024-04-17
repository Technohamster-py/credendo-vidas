from django.db import models


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('e-mail')
    nickname = models.CharField('Никнейм', max_length=50)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('Заголовок', max_length=150)
    body = models.TextField('Тело статьи')
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    #date_published = models.DateTimeField('Дата публикации', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')
    cover = models.ImageField('Обложка', blank=True)
    is_published = models.BooleanField('Опубликовать', default=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

# Create your models here.
