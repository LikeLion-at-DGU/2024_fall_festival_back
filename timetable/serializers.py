from rest_framework import serializers
from .models import *

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        fields = ['day','fire_count']

class TimetableDetailSerializer(serializers.ModelSerializer):
    show = TimetableSerializer()  # Timetable과 연결된 정보도 포함

    class Meta:
        model = TimetableDetail
        fields = '__all__'