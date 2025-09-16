# payroll/admin.py
from django.contrib import admin
from .models import PayPeriod, Payslip

@admin.register(PayPeriod)
class PayPeriodAdmin(admin.ModelAdmin):
    list_display = ('start_date','end_date','is_closed')

@admin.register(Payslip)
class PayslipAdmin(admin.ModelAdmin):
    list_display = ('employee','pay_period','net_pay','generated_at')
    list_filter  = ('pay_period',)
