# Generated by Django 3.2.9 on 2021-12-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211105_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='slug',
            field=models.SlugField(default='', max_length=150, verbose_name='Url'),
        ),
    ]