from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PayPeriodViewSet, PayslipViewSet

router = DefaultRouter()
router.register('periods', PayPeriodViewSet, basename='period')
router.register('payslips', PayslipViewSet, basename='payslip')

urlpatterns = [
    path('', include(router.urls)),
]
