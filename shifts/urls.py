from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShiftViewSet

router = DefaultRouter()
router.register('', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
