from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from .views import BoothViewSet, BoothDetailViewSet, BoothDetailListViewSet

app_name = 'booth'

router = SimpleRouter(trailing_slash=False)
router.register(r'booth', BoothViewSet, basename='booth')

urlpatterns = [
    path('v1/', include(router.urls)),  # 'api/v1/' 경로로 ViewSet 엔드포인트 등록
    path('v1/booth/detail/', BoothDetailListViewSet.as_view(), name='booth-detail-list'),
    path('v1/booth/detail/<int:id>/', BoothDetailViewSet.as_view(), name='booth_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
