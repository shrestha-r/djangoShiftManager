from django.db import models
from shifts.models import Shift
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Timesheet(models.Model):
    shift = models.OneToOneField(Shift, on_delete=models.CASCADE)
    clock_in_time = models.TimeField()
    clock_out_time = models.TimeField()
    break_taken = models.PositiveIntegerField(default=0)
    employee_notes = models.TextField(blank=True)
    manager_notes = models.TextField(blank=True)
    approval_status = models.CharField(max_length=20, choices=[('pending','Pending'),('approved','Approved'),('rejected','Rejected')], default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_timesheets')
    approved_at = models.DateTimeField(null=True, blank=True)

    @property
    def actual_hours_worked(self):
        start = datetime.combine(self.shift.date, self.clock_in_time)
        end = datetime.combine(self.shift.date, self.clock_out_time)
        if end <= start: end += timedelta(days=1)
        return (end - start).total_seconds()/3600 - (self.break_taken/60)

    @property
    def actual_pay(self):
        return self.actual_hours_worked * self.shift.hourly_rate

    def __str__(self):
        return f"Timesheet for {self.shift}"
