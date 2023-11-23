from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()