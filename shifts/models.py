from django.db import models
from employees.models import Employee
from positions.models import JobPosition
from datetime import datetime, timedelta

class Shift(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_minutes = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('scheduled','Scheduled'),('completed','Completed'),('cancelled','Cancelled'),('no_show','No Show')], default='scheduled')
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def scheduled_hours(self):
        start = datetime.combine(self.date, self.start_time)
        end = datetime.combine(self.date, self.end_time)
        if end <= start:
            end += timedelta(days=1)
        return (end - start).total_seconds()/3600 - (self.break_minutes/60)

    @property
    def calculated_pay(self):
        return self.scheduled_hours * self.hourly_rate

    def __str__(self):
        return f"{self.employee.user.get_full_name()} - {self.job_position.title} ({self.date})"
