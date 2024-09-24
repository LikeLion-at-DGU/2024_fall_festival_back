from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booth(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=20)
    is_night = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    host = models.CharField(max_length=50)
    like = models.ManyToManyField(User, related_name="likes", blank=True)
    like_count = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name