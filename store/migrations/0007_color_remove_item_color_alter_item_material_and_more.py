# Generated by Django 4.2.3 on 2023-07-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_item_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='color',
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.CharField(blank=True, max_length=30, verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.ManyToManyField(to='store.color'),
        ),
    ]
