# Generated by Django 4.0.10 on 2023-04-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_room_long_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='long_description',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
