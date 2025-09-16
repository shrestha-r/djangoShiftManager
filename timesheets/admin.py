# timesheets/admin.py
from django.contrib import admin
from .models import Timesheet

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('shift','approval_status','submitted_at')
    list_filter  = ('approval_status',)
