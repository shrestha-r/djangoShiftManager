# employees/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user','employee_id','agency','employment_status')
    search_fields = ('user__username','employee_id')
