from rest_framework import serializers
from .models import *

class TimetableDeatailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        fields = ['day','fire_count']