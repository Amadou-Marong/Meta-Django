from django.db import models

# Create your models here.
SHIFTS = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class LogForm(models.Model):
    first_name = models.CharField(max_length=200, required=True)
    last_name = models.CharField(max_length=200, required=True)
    shift = models.CharField(max_length=1, choices=SHIFTS, required=True)
    time_log = models.TimeField(auto_now_add=True)