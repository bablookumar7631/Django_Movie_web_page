# Generated by Django 4.1.6 on 2023-09-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allmovie',
            name='links_down_1',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='allmovie',
            name='links_down_2',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='allmovie',
            name='links_name_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='allmovie',
            name='links_name_2',
            field=models.CharField(default='', max_length=200),
        ),
    ]