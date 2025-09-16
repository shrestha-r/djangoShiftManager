# positions/admin.py
from django.contrib import admin
from .models import JobPosition

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title','client','location','hourly_rate')
    list_filter  = ('client',)
