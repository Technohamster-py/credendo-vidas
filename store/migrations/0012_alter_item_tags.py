# Generated by Django 4.2.3 on 2023-08-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='store.tag'),
        ),
    ]
