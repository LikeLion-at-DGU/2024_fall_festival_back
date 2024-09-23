from django.urls import path, include
from .views import FireViewSet

fire_list = FireViewSet.as_view({
    'post': 'increase_fire'
})

urlpatterns = [
    path('timetable/<str:day>/fire/', fire_list, name='increase_fire'),
]