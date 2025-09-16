from rest_framework import viewsets, permissions
from .models import JobPosition
from .serializers import JobPositionSerializer

class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()  # <— add this
    serializer_class = JobPositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        agency_id = self.request.user.employee.agency_id
        return JobPosition.objects.filter(client__agency_id=agency_id)
