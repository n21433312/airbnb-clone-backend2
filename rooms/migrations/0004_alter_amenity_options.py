# Generated by Django 4.1.7 on 2023-03-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_name_alter_amenity_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
    ]
