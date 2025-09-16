from rest_framework import serializers
from .models import JobAgency

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAgency
        fields = '__all__'
