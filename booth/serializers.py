from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = '__all__'

class BoothDetailSerializer(serializers.ModelSerializer):
    booth = serializers.PrimaryKeyRelatedField(queryset=Booth.objects.all())

    class Meta:
        model = BoothDetail
        fields = '__all__'