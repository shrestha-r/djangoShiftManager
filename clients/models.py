from django.db import models
from agency.models import JobAgency

class Client(models.Model):
    agency = models.ForeignKey(JobAgency, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.company_name
