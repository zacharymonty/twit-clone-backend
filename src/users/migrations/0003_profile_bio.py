# Generated by Django 3.1.2 on 2020-11-02 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Bio goes here', max_length=240),
        ),
    ]
