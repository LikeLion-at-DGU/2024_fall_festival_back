from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BoothDetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoothDetail
        fields = ['image']  # BoothDetail의 image 필드만 포함


class BoothSerializer(serializers.ModelSerializer):
    # BoothDetail의 image 필드만 포함
    details_image = BoothDetailImageSerializer(source='details', read_only=True) 

    class Meta:
        model = Booth
        fields = ['id', 'day', 'category', 'latitude', 'longitude', 
                  'location', 'is_night', 'name', 'description', 'host', 
                  'like_count', 'start_time', 'end_time', 'is_reservable', 'details_image']


class BoothDetailSerializer(serializers.ModelSerializer):
    booth = serializers.PrimaryKeyRelatedField(queryset=Booth.objects.all())

    class Meta:
        model = BoothDetail
        fields = '__all__'