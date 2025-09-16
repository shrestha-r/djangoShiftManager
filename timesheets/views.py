from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Timesheet
from .serializers import TimesheetSerializer

class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all()
    serializer_class = TimesheetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        emp = self.request.user.employee
        if self.request.user.is_staff:
            return Timesheet.objects.filter(shift__employee__agency=emp.agency)
        return Timesheet.objects.filter(shift__employee=emp)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        ts = self.get_object()
        ts.approval_status = 'approved'
        ts.approved_by = request.user
        ts.approved_at = datetime.now()
        ts.save()
        return Response(self.get_serializer(ts).data, status=status.HTTP_200_OK)
from rest_framework import viewsets, permissions
from .models import Timesheet
from .serializers import TimesheetSerializer
from datetime import datetime

class TimesheetViewSet(viewsets.ModelViewSet):
    queryset = Timesheet.objects.all()  # <— add this
    serializer_class = TimesheetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        emp = self.request.user.employee
        if self.request.user.is_staff:
            return Timesheet.objects.filter(shift__employee__agency=emp.agency)
        return Timesheet.objects.filter(shift__employee=emp)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        ts = self.get_object()
        ts.approval_status = 'approved'
        ts.approved_by = request.user
        ts.approved_at = datetime.now()
        ts.save()
        return Response(self.get_serializer(ts).data)
