from django.db import models
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

# Create your models here.
class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    image = models.ImageField()
    description = models.TextField(max_length=200)
    info = models.TextField(max_length=200)
    insta_id = models.CharField(max_length=50)
    insta_link = models.URLField(max_length=200)
    