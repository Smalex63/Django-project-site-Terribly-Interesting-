# Generated by Django 3.2.9 on 2021-12-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='main.Category', verbose_name='Категории'),
        ),
    ]
