# Generated by Django 2.2.5 on 2021-04-21 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_remove_room_cityy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='city',
        ),
    ]