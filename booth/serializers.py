from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class BoothSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booth
        fields = ['id', 'day', 'category', 'latitude', 'longitude', 
                  'location', 'is_night', 'name', 'description', 'host', 
                  'start_time', 'end_time', 'is_reservable', 'thumbnail']


class BoothDetailSerializer(serializers.ModelSerializer):
    # BoothDetail 모델의 필드를 추가
    booth = serializers.IntegerField(source='id', read_only=True)
    is_night = serializers.BooleanField(source='details.is_night', read_only=True)
    day = serializers.CharField(source='details.day', read_only=True)
    description = serializers.CharField(source='details.description', read_only=True)
    start_time = serializers.DateTimeField(source='details.start_time', read_only=True)
    end_time = serializers.DateTimeField(source='details.end_time', read_only=True)
    is_reservable = serializers.BooleanField(source='details.is_reservable', read_only=True)
    details_image = serializers.SerializerMethodField()

    detail_description = serializers.CharField(source='details.detail_description',read_only=True)
    entrace_fee = serializers.IntegerField(source='details.entrace_fee',read_only=True)
    menus = serializers.CharField(source='details.menus',read_only=True)
    tabling_link = serializers.CharField(source='details.tabling_link',read_only=True)
    insta_id = serializers.CharField(source='details.insta_id',read_only=True)
    insta_link = serializers.CharField(source='details.insta_link',read_only=True)
   
    class Meta:
        model = Booth
        fields = '__all__'

    def get_details_image(self, obj):
        request = self.context.get('request')
        images = obj.images.all()  # OneToOne 관계에서 booth의 이미지를 가져옴

        # URL을 생성
        image_urls = [request.build_absolute_uri(image.image.url) for image in images]
        return image_urls
        