from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPositionViewSet

router = DefaultRouter()
router.register('', JobPositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
