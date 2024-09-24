from django.urls import path, include
from .views import FireViewSet, TimetableDetailViewSet

fire_list = FireViewSet.as_view({
    'post': 'increase_fire'
})
timetable_detail = TimetableDetailViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('timetable/fire/', fire_list, name='increase_fire'),
    path('timetable/<int:pk>/', timetable_detail, name='timetable_detail'),
]
