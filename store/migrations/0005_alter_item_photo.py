# Generated by Django 4.2.3 on 2023-07-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/store/item_images/'),
        ),
    ]
