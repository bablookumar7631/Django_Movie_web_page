# Generated by Django 4.1.6 on 2023-09-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_moviecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='comment',
            field=models.TextField(),
        ),
    ]