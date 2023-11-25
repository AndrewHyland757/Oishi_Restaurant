from django.db import models
#from allauth.models import CustomUser as User
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

time_choices = (
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("01:00", "01:00"),
    ("01:30", "01:30"),
    ("02:00", "02:00"),
    ("02:30", "02:30"),
    ("03:00", "03:00"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    )


guest_choices = (
    (1, "1 guest"), 
    (2, "2 guests"),
    (3, "3 guests"), 
    (4, "4 guests"),
    (5, "5 guests"),
    (6, "6 guests"),
    )



class Table(models.Model):
    table_no = models.IntegerField(unique=True)
    table_seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_no}"




class Booking(models.Model):
    date = models.DateField()
    time = models.CharField(default = '12:00', max_length=100, choices = time_choices)
    guests = models.IntegerField(default = 1, choices = guest_choices)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    

    def __str__(self):
        return f"{self.customer}'s reservation on {self.date}"
        
    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("Please choose a valid date")
        #overlapping_bookings = Booking.objects.filter(date= self.date, time=self.time, table=self.table)
    

