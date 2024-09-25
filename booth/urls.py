from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import BoothViewSet

app_name = 'booth'

router = SimpleRouter(trailing_slash=False)
router.register(r'booth', BoothViewSet, basename='booth')

urlpatterns = [
    path('api/v1/', include(router.urls)),  # 'api/v1/' 경로로 ViewSet 엔드포인트 등록
]
