# Generated by Django 3.2.9 on 2021-12-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]
