from rest_framework import viewsets, permissions
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Managers of an agency see all employees in that agency
        agency_ids = self.request.user.employee.agency_id
        return Employee.objects.filter(agency_id=agency_ids)
