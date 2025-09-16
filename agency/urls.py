from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agency.views import AgencyViewSet

router = DefaultRouter()
router.register('', AgencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
