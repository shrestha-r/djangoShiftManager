from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PayPeriod, Payslip
from .serializers import PayPeriodSerializer, PayslipSerializer
from employees.models import Employee
from timesheets.models import Timesheet
from datetime import datetime

class PayPeriodViewSet(viewsets.ModelViewSet):
    queryset = PayPeriod.objects.all()  # <— add this
    serializer_class = PayPeriodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        agency_id = self.request.user.employee.agency_id
        return PayPeriod.objects.filter(agency_id=agency_id)

class PayslipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payslip.objects.all()  # <— add this
    serializer_class = PayslipSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def generate(self, request):
        # same generate logic
        ...
