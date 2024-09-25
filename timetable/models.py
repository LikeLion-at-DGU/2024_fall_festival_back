<<<<<<< HEAD

# Create your models here.
=======
>>>>>>> 2ddf488d530e821454c72245f60c2b7cf8300569
from django.db import models
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

# Create your models here.
class Timetable(models.Model):
<<<<<<< HEAD
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
    ]
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    category = models.CharField(max_length=20)
=======
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
>>>>>>> 2ddf488d530e821454c72245f60c2b7cf8300569
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
<<<<<<< HEAD
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    insta_id = models.CharField(max_length=50, blank=True, null=True)
    insta_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.day} - {self.name}"
    
class Fire(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
    ]
    
    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)
    fire_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.day} - Fire Count: {self.fire_count}"
    
class TimetableDetail(models.Model):
    show = models.ForeignKey(Timetable, on_delete=models.CASCADE)  # Timetable과 연결
    main_song = models.CharField(max_length=100, blank=True, null=True)  # 메인 곡
    show_info = models.TextField(blank=True, null=True)  # 공연 정보
    insta_id = models.CharField(max_length=50, blank=True, null=True)  # 인스타 아이디
    insta_link = models.URLField(blank=True, null=True)  # 인스타 링크
    youtube_link = models.URLField(blank=True, null=True)  # 유튜브 링크

    def __str__(self):
        return f"Detail for {self.show.name}"
=======
    image = models.ImageField()
    description = models.TextField(max_length=200)
    info = models.TextField(max_length=200)
    insta_id = models.CharField(max_length=50)
    insta_link = models.URLField(max_length=200)
    
>>>>>>> 2ddf488d530e821454c72245f60c2b7cf8300569
