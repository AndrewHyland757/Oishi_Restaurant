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
    number_of_guests = models.IntegerField(default = 1, choices = guest_choices)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # change to user_name
    guest_name = models.CharField(max_length=100, null=True) # change to guest_user_name
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    
    """
    def user_field(self): # don't show customer_name if guest_name is populated
        if guest_name == None:
            del guest_name
        return  self
    """
    """ 

    def change_guest_name_to_customer_name(self):
        
        #If booking is made as a guest first and then an account is set up with the same email, 
        #the older bookings associated with that email aare updated to include the new registered customer name
        

        customer_name = self.customer_name
        email = self.email
        guest_name = self.guest_name

        user_bookings = Booking.objects.filter(email)  # all instances related to the email 

        user_bookings_customer = Booking.objects.filter(customer_name) # all with a customer_name
        user_bookings_guest = Booking.objects.filter(guest_name)  # all with a guest_name
    
        if user_bookings_guest and 

            if booking.customer_name != None:
                pass
            else:
                booking.customer_name = customer_name
                del guest_name
    """

    def __str__(self):
        if  self.guest_name == None:
            return f"{self.customer_name}'s reservation on {self.date}"
        else:
            return f"{self.guest_name}'s reservation on {self.date}"
        
    def clean(self):
        if self.date < timezone.now().date():
            raise ValidationError("Please choose a valid date")
        
    

