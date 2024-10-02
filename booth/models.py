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
    is_reservable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class BoothDetail(models.Model):
    id = models.AutoField(primary_key=True)     # 부스 디테일의 고유 id
    booth = models.OneToOneField(Booth, on_delete=models.CASCADE, related_name='details')    # 부스 id를 왜래키로 참조
    detail_description = models.TextField(blank=True)   # 부스 상세 설명
    entrace_fee = models.IntegerField(default=0)        # 입장료
    menus = models.TextField(blank=True)                # 메뉴 정보
    tabling_link = models.TextField(blank=True)         # 테이블링 서비스로 이동하는 링크
    insta_id = models.CharField(max_length=50, blank=True)   # 인스타그램 아이디
    insta_link = models.TextField(blank=True)               # 인스타그램 링크
    image = models.ImageField(upload_to="booth/", blank=True, null=True)    # 부스 이미지
    like_count = models.IntegerField(default=0)                        # 부스 좋아요
    is_reservable = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.like_count = self.booth.like_count
        super().save(*args, **kwargs)