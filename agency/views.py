from rest_framework import viewsets, permissions
from .models import JobAgency
from .serializers import AgencySerializer

class AgencyViewSet(viewsets.ModelViewSet):
    queryset = JobAgency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [permissions.IsAuthenticated]
