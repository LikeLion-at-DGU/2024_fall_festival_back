# Generated by Django 5.1.1 on 2024-10-05 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0004_remove_boothdetail_thumbnail_booth_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='booth',
        ),
    ]
