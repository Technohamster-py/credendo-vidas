# Generated by Django 4.2.3 on 2024-04-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_item_last_status_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=30, verbose_name='Размер'),
        ),
    ]