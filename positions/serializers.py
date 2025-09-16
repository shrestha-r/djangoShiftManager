from rest_framework import serializers
from .models import JobPosition

class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'
