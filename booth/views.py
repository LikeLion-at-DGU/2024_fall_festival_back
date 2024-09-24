from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Booth
from .serializers import BoothSerializer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

class BoothViewSet(viewsets.ModelViewSet):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer
    
    def get_queryset(self):
        # 기본 queryset 설정
        queryset = super().get_queryset()

        # URL 쿼리 파라미터에서 day 값을 가져옴
        day = self.request.query_params.get('day')

        # day가 None이면 'Mon'으로 기본 설정
        if day is None:
            day = 'Mon'

        # day 값을 기반으로 필터링
        queryset = queryset.filter(day=day)
        
        return queryset



