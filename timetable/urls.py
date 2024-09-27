from django.urls import path, include
from .views import FireViewSet, TimetableDetailViewSet, TimetableViewSet

fire_list = FireViewSet.as_view({
    'post': 'increase_fire'
})
timetable_list = TimetableViewSet.as_view({
    'get': 'list'
})
timetable_now = TimetableViewSet.as_view({
    'get': 'now'
})
timetable_detail = TimetableDetailViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('timetable/fire/', fire_list, name='increase_fire'),
    path('timetable/', timetable_list, name='timetable_list'),
    path('timetable/now', timetable_now, name='timetable_now'),
    path('timetable/<int:pk>/', timetable_detail, name='timetable_detail'),
]
