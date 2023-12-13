from django.db import models
from django.contrib.auth.models import User

time_choices = (
    ("12:00", "12:00"),
    ("01:00", "01:00"),
    ("02:00", "02:00"),
    ("03:00", "03:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
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
    """
    This model containg the tables in the restaurant
    """
    table_no = models.IntegerField(unique=True)
    table_seats = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Table {self.table_no}"


class Booking(models.Model):
    """
    This model contains the information for each booking
    """
    date = models.DateField()
    time = models.CharField(
        default='12:00', max_length=100, choices=time_choices)
    number_of_guests = models.IntegerField(
        default=1, choices=guest_choices)
    customer_name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=100, null=True)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True, blank=False)

    def __str__(self):
        if self.guest_name is None:
            return f"{self.customer_name}'s reservation on {self.date}"
        else:
            return f"{self.guest_name}'s reservation on {self.date}"