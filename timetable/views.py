from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Fire
from .serializers import FireSerializer
from django.utils import timezone  # timezone 사용
from datetime import datetime

class FireViewSet(viewsets.ViewSet):
    """
    Mon, Tue별 '🔥' 카운트를 관리하는 ViewSet
    """

    @action(detail=False, methods=['post'], url_path='timetable/(?P<day>Mon|Tue)/fire')
    def increase_fire(self, request, day=None):
        """
        '🔥' 버튼을 누르면 해당 요일의 fire_count가 1 증가
        """
        # 요일 검증 로직 추가
        if day not in ['Mon', 'Tue']:
            return Response({"error": "Invalid day. Only 'Mon' or 'Tue' are allowed."}, status=400)
        # 해당 요일에 해당하는 Fire 객체를 찾거나 생성
        fire, created = Fire.objects.get_or_create(day=day)
        
        # fire_count 증가
        fire.fire_count += 1
        fire.save()

        serializer = FireSerializer(fire)
        return Response(serializer.data)
