from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/agency/', include('agency.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/employees/', include('employees.urls')),
    path('api/positions/', include('positions.urls')),
    path('api/shifts/', include('shifts.urls')),
    path('api/timesheets/', include('timesheets.urls')),
    path('api/payroll/', include('payroll.urls')),
]
