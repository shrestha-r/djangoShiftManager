from django.db import models
from django.contrib.auth.models import User
from agency.models import JobAgency

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(JobAgency, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    national_insurance_number = models.CharField(max_length=20)
    bank_account_number = models.CharField(max_length=20)
    sort_code = models.CharField(max_length=10)
    hourly_rate_default = models.DecimalField(max_digits=6, decimal_places=2)
    employment_status = models.CharField(max_length=20, choices=[('active','Active'),('inactive','Inactive'),('terminated','Terminated')], default='active')
    date_hired = models.DateField()
    skills = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"
