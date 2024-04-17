# Generated by Django 4.2.3 on 2024-04-17 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('nickname', models.CharField(max_length=50, verbose_name='Никнейм')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Тело статьи')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
                ('cover', models.ImageField(blank=True, upload_to='', verbose_name='Обложка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]