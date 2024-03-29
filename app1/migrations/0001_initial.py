# Generated by Django 4.1.7 on 2023-09-12 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('scr_id', models.AutoField(primary_key=True, serialize=False)),
                ('scr_title', models.CharField(max_length=100)),
                ('scr_image', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Allmovie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_image', models.ImageField(default='', upload_to='')),
                ('Full_name', models.CharField(default='', max_length=100)),
                ('language', models.CharField(default='', max_length=100)),
                ('release_year', models.IntegerField(default=0)),
                ('quality', models.CharField(default='', max_length=100)),
                ('pixel', models.CharField(default='', max_length=100)),
                ('size', models.CharField(default='', max_length=100)),
                ('stars_name', models.CharField(default='', max_length=255)),
                ('director', models.CharField(default='', max_length=255)),
                ('storyline', models.TextField(default='')),
                ('Screenshot_img', models.ManyToManyField(default=None, to='app1.screenshot')),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
