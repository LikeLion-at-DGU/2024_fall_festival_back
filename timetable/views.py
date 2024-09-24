from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Fire, Timetable, TimetableDetail
from .serializers import FireSerializer, TimetableSerializer, TimetableDetailSerializer
from django.utils import timezone  # timezone 사용
from datetime import datetime

class FireViewSet(viewsets.ViewSet):
    """
    Mon, Tue별 '🔥' 카운트를 관리하는 ViewSet
    """

    @action(detail=False, methods=['post'], url_path='timetable/(?P<day>Mon|Tue)/fire')
    def increase_fire(self, request):
        """
        '🔥' 버튼을 누르면 해당 요일의 fire_count가 1 증가
        """
        day = request.query_params.get('day')
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


    
class TimetableDetailViewSet(viewsets.ModelViewSet):
    """
    Timetable과 관련된 세부 공연 정보를 제공하는 ViewSet
    """
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

    @action(detail=True, methods=['get'], url_path='detail')
    def get_detail(self, request, pk=None):
        """
        특정 Timetable과 연결된 ShowDetail 정보를 반환
        """
        # Timetable의 pk와 연결된 ShowDetail 객체 가져오기
        show_detail = get_object_or_404(TimetableDetail, show__id=pk)
        serializer = TimetableDetailSerializer(show_detail)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Timetable의 id에 해당하는 정보를 반환 (즉, 디테일 페이지로 이동)
        """
        timetable = get_object_or_404(Timetable, pk=pk)
        serializer = TimetableSerializer(timetable)
        return Response(serializer.data)