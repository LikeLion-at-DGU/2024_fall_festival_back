from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Booth, BoothDetail
from .serializers import BoothSerializer, BoothDetailSerializer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.http import JsonResponse


# Booth 필터 클래스 정의
class BoothFilter(django_filters.FilterSet):
    class Meta:
        model = Booth
        fields = {
            'day': ['exact'],           # 날짜
            'category': ['exact'],      # 카테고리 필터
            'location': ['exact'],      # 위치 필터
            'is_night': ['exact'],      # True 또는 False 필터
        }

class BoothViewSet(viewsets.ModelViewSet):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoothFilter
    
    def get_queryset(self):
        # 기본 queryset 설정
        queryset = super().get_queryset()

        # URL 쿼리 파라미터에서 day 값을 가져옴
        day = self.request.query_params.get('day')
        category = self.request.query_params.get('category')
        location = self.request.query_params.get('location')
        is_night = self.request.query_params.get('is_night')
        is_reservable = self.request.query_params.get('is_reservable')  # 예약 가능 필터

        # day가 None이면 'Mon'으로 기본 설정
        if day is None:
            day = 'Mon'

        # day 값을 기반으로 필터링
        queryset = queryset.filter(day=day)

        if category:
            queryset = queryset.filter(category=category)

        if location:
            queryset = queryset.filter(location=location)

        if is_night is not None:
            queryset = queryset.filter(is_night=is_night.lower() == 'true')

        # 예약 가능 여부 필터링 추가
        if is_reservable is not None:
            queryset = queryset.filter(is_reservable=is_reservable.lower() == 'true')


        queryset = queryset.order_by('name')
        
        return queryset

class BoothDetailViewSet(generics.RetrieveUpdateAPIView):
    queryset = BoothDetail.objects.all()
    serializer_class = BoothDetailSerializer
    lookup_field = 'id'

class BoothDetailListViewSet(generics.ListCreateAPIView):
    queryset = BoothDetail.objects.all()
    serializer_class = BoothDetailSerializer
