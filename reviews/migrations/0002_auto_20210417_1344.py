# Generated by Django 2.2.5 on 2021-04-17 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='cleanlineless',
            new_name='cleanliness',
        ),
    ]
