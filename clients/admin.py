# clients/admin.py
from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name','contact_person','email')
    list_filter  = ('agency',)
