# agency/admin.py
from django.contrib import admin
from .models import JobAgency

@admin.register(JobAgency)
class JobAgencyAdmin(admin.ModelAdmin):
    list_display = ('name','contact_email','phone','created_at')
