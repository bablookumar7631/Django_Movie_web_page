# Generated by Django 4.1.6 on 2023-09-16 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_moviecomment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allmovie',
            name='Screenshot_img',
        ),
        migrations.AddField(
            model_name='allmovie',
            name='Screenshot_img',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app1.screenshot'),
        ),
    ]