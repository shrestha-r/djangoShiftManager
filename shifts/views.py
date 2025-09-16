from rest_framework import viewsets, permissions
from .models import Shift
from .serializers import ShiftSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()  # <— add this
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        emp = self.request.user.employee
        if self.request.user.is_staff:
            return Shift.objects.filter(employee__agency=emp.agency)
        return Shift.objects.filter(employee=emp)

    def perform_create(self, serializer):
        emp = self.request.user.employee
        serializer.save(employee=emp, hourly_rate=serializer.validated_data['job_position'].hourly_rate)
