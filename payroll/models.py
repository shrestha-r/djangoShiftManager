from django.db import models
from employees.models import Employee
from timesheets.models import Timesheet

class PayPeriod(models.Model):
    agency = models.ForeignKey('agency.JobAgency', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.start_date} – {self.end_date}"

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period = models.ForeignKey(PayPeriod, on_delete=models.CASCADE)
    total_hours = models.DecimalField(max_digits=8, decimal_places=2)
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payslip: {self.employee.user.get_full_name()} - {self.pay_period}"
