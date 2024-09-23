from rest_framework import serializers
from .models import *

class TimetabledetailSerializer(serializers.ModelSerializer):
    class Meata:
        model = Timetable
        fields = '__all__'