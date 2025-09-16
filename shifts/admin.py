# shifts/admin.py
from django.contrib import admin
from .models import Shift

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('employee','job_position','date','start_time','end_time','status')
    list_filter  = ('status','job_position')
