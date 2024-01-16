from django.db import models
import datetime

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    patient_ID = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.patient_ID)