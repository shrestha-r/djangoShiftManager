from rest_framework import serializers
from .models import PayPeriod, Payslip

class PayPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayPeriod
        fields = '__all__'

class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'
