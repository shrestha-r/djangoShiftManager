from django.db import models

class JobAgency(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
