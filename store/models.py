from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField('Названиие категории', max_length=20)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTМeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField('Название тега', max_length=15)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Color(models.Model):
    color = models.CharField('Цвет', max_length=20)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color

class Item(models.Model):
    STORED = True
    ACTIVE = False

    STATUS_CHOISES = [
        (STORED, 'На складе'),
        (ACTIVE, 'В работе')
    ]

    name = models.CharField('Название', max_length=100)
    photo = models.ImageField(upload_to='store/item_images/', default="No-Image-Placeholder.svg")
    place = models.CharField('Место на складе', max_length=50)
    size = models.CharField('Размер', max_length=30)
    material = models.CharField('Материал', max_length=30, blank=True)
    status = models.BooleanField('Статус', choices=STATUS_CHOISES)
    color = models.ManyToManyField(Color)
    last_status_change = models.DateTimeField('Последнее изменение статуса')
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True, default=14)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Operation(models.Model):
    TAKE = 'TAKE'
    RETURN = 'RETURN'

    ACTION_CHOISES = [
        (TAKE, 'Взял'),
        (RETURN, 'Вернул')
    ]

    first_name = models.CharField('Имя', max_length=15)
    last_name = models.CharField('Фамилия', max_length=20)
    action = models.CharField('Тип операции', max_length=6, choices=ACTION_CHOISES, default=TAKE)
    date = models.DateTimeField('Время операции')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.action} "{self.item}" в {self.date}'

