# Generated by Django 5.1.1 on 2024-09-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_fire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fire',
            name='fire',
        ),
        migrations.AlterField(
            model_name='fire',
            name='day',
            field=models.DateTimeField(unique=True),
        ),
    ]