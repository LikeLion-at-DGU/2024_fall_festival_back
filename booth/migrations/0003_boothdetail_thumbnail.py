# Generated by Django 5.1.1 on 2024-10-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0002_rename_is_nignt_boothdetail_is_night_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boothdetail',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='booth/'),
        ),
    ]