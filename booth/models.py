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
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_reservable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class BoothDetail(models.Model):
    id = models.AutoField(primary_key=True)     # 부스 디테일의 고유 id
    booth = models.OneToOneField(Booth, on_delete=models.CASCADE, related_name='details')    # 부스 id를 외래키로 참조
    detail_description = models.TextField(blank=True)   # 부스 상세 설명
    entrace_fee = models.IntegerField(default=0)        # 입장료
    menus = models.TextField(blank=True)                # 메뉴 정보
    tabling_link = models.TextField(blank=True)         # 테이블링 서비스로 이동하는 링크
    insta_id = models.CharField(max_length=50, blank=True)   # 인스타그램 아이디
    insta_link = models.TextField(blank=True)               # 인스타그램 링크
    image = models.ImageField(upload_to="booth/", blank=True, null=True)    # 부스 이미지
    is_night = models.BooleanField(default=False, blank=True)       # 낮/밤 여부
    is_reservable = models.BooleanField(default=False, blank=True)  # 예약 가능 여부
    location = models.CharField(max_length=20, blank=True)          # 위치
    category = models.CharField(max_length=20, blank=True)          # 부스 종류
    host = models.CharField(max_length=50, blank=True)              # 운영 주체
    start_time = models.TimeField(blank=True)                     # 시작 시간
    end_time = models.TimeField(blank=True)                       # 종료 시간

    def save(self, *args, **kwargs):
        self.is_night = self.booth.is_night
        self.is_reservable = self.booth.is_reservable
        self.location = self.booth.location
        self.category = self.booth.category
        self.host = self.booth.host
        self.start_time = self.booth.start_time
        self.end_time = self.booth.end_time
        super().save(*args, **kwargs)