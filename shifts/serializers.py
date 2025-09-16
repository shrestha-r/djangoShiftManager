from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    scheduled_hours = serializers.ReadOnlyField()
    calculated_pay = serializers.ReadOnlyField()

    class Meta:
        model = Shift
        fields = '__all__'
