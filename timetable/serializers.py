from rest_framework import serializers
from .models import *

<<<<<<< HEAD
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
=======
class TimetabledetailSerializer(serializers.ModelSerializer):
    class Meata:
        model = Timetable
>>>>>>> 2ddf488d530e821454c72245f60c2b7cf8300569
        fields = '__all__'