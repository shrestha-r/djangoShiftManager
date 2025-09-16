from django.db import models
from clients.models import Client

class JobPosition(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    required_skills = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.client.company_name}"
