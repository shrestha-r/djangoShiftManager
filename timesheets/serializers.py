from rest_framework import serializers
from .models import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    actual_hours_worked = serializers.ReadOnlyField()
    actual_pay = serializers.ReadOnlyField()

    class Meta:
        model = Timesheet
        fields = '__all__'
