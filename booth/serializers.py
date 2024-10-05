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
    booth = serializers.PrimaryKeyRelatedField(queryset=Booth.objects.all())
    details_image = serializers.SerializerMethodField()
    
    class Meta:
        model = BoothDetail
        fields = '__all__'

    def get_details_image(self, obj):
        # BoothDetail과 연결된 Booth의 id를 사용해 Image 모델에서 booth_id로 필터링
        request = self.context.get('request')  # request 객체를 가져옵니다.
        images = obj.booth.images.all()  # 이미지를 가져옵니다.
        
        # 각 이미지 객체의 URL을 생성합니다.
        image_urls = [request.build_absolute_uri(image.image.url) for image in images]
        
        return image_urls  # URL 리스트 형태로 반환
        