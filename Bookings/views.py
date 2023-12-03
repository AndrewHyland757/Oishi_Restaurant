from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib import messages
from .forms import BookingForm, BookingFormNotLoggedIn, CancelBookingForm
from django.utils import timezone



def get_booked_tables(requested_date, requested_time):
    """
    Returns any tables in the BOOKING MODEL assigned to requested time/date. 
    """
    
    # Gets all the instances from the Booking model with the same time/date as the users requested time/date
    filtered_booking_data = Booking.objects.filter(time=requested_time,
        date=requested_date)

    # Creates a list from the "table" field in each iteration in the filtered_booking_data
    booked_tables = [booking.table for booking in filtered_booking_data] 
    
    # Returns the booked tables
    return booked_tables


def get_tables():
    """
    Returns all tables from the TABLE MODEL
    """
    tables = Table.objects.all()
    return tables


def assign_table(available_tables, requested_guests):
    """
    This function takes the available tables at users requested time/date and assigns the best size table according to the number of guests. 
    The parameters "available_tables" and "requested_guests" will be defined in the home function. 
    """
    # The available_tables are sorted according to their number of seats
    available_tables = sorted(available_tables, key=lambda table:int(table.table_seats)) # lambda creates a function in one line

    # A loop to iterate through the available_tables starting with lowest seat number
    for table in available_tables:

        # If the iterated table has the same amount of seats as requested guests it is the perfect fit and assigned first
        if int(table.table_seats) >= int(requested_guests):  
            return table
        
        # If the iterated table has the same amount of seats plus one spare it is next assigned. 
        elif int(table.table_seats) == sum([int(requested_guests), 1]): 
            return table

        # If the iterated table has the same amount of seats plus two spare it is assigned
        elif int(table.table_seats) == sum([int(requested_guests), 2]): 
            return table

        # If the iterated table has the same amount of seats plus three spare it is assigned
        elif int(table.table_seats) == sum([int(requested_guests), 3]):
            return table
        
    # If there will be more than three empty seats at a booking it is deemed inefficient and error message displayed
    message = f"Unfortunately, we have no available tabele for {requested_guests} at {requested_time} on {requested_date}."
    context = {
        "message" : message
    }
    return render(request, "index.html", context )

   
def home(request):
    """
    Function to render the home page and handle the booking form
    """

    # Checks if user is logged in, and if so, uses the appropriate form 
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)

            if form.is_valid():
                form_instance = form.save(commit=False)

                # Populate the booking instance customer_name field
                form_instance.customer_name = request.user

                # Populate the booking instance email field
                form_instance.email = request.user.email

                # Create some variables from the form displayed fields
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('number_of_guests')
             
                
                # List of tables from the BOOKING MODEL already assigned to requested time/date
                booked_tables = get_booked_tables(requested_date, requested_time)
               
                # List of tables in the TABLE MODEL excluding the tables assigned in BOOKING MODEL at requested time/date
                available_tables = Table.objects.exclude(pk__in = [table.pk for table in booked_tables])

                # Checks if there is at least one table available
                if available_tables.count() <= 0:
                    message = f"Unfortunately we fully booked at {requested_time} on {requested_date}."
                    messages.success(request, message)
                
                else:
                    # Calls the assign_table function to choose the most efficient table for the number of guests
                    form_instance.table = assign_table(available_tables, requested_guests)
                    form_instance.save()

                    # Redirects to the View Bookings page 
                    #return redirect('view_bookings') 
                    message = f"Your booking has been made on the {requested_date} at {requested_time} for {requested_guests} guest(s)."
                    messages.success(request, message)
        else:
            form = BookingForm()

    else:
        # If the user is not logged in/registered, the guest booking form will be used which contains extra fields
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)

            if form.is_valid():
                form_instance = form.save(commit=False)

                # Create some variables from the form displayed fields
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('number_of_guests')
             
                # List of tables from the BOOKING MODEL already assigned to requested time/date
                booked_tables = get_booked_tables(requested_date, requested_time)
               
                # List of tables in the TABLE MODEL excluding the tables assigned in BOOKING MODEL at requested time/date
                available_tables = Table.objects.exclude(pk__in = [table.pk for table in booked_tables])

                # Checks if there is at least one table available
                if available_tables.count() <= 0:
                    message = f"Unfortunately, we fully booked at {requested_time} on {requested_date}."
                   
                    messages.success(request, message)
                
                else:
                    # Calls the assign_table function to choose the most efficient table for the number of guests
                    form_instance.table = assign_table(available_tables, requested_guests)

                    # Save sthe instance 
                    form_instance.save()

                    # Displays success message
                    message = f"Your table  for {requested_guests} is booked at {requested_time} on {requested_date}."
                    messages.success(request, message)

                    # Cleans form fields
                    form = BookingFormNotLoggedIn()
                    
        else:
            form = BookingFormNotLoggedIn()

    context = {'form': form}
    return render(request, "index.html", context)



@login_required(login_url='account_login')
def view_bookings(request):
    """
    Gets the reservations from the logged in user based on their email or user name (incase the superuser hasn't used an email)
    If bookings were made as a guest before the user registered an account, it gets these bookings by the their email. 
    """

    # Variable containing all bookings associated with the email used
    bookings_from_emails = Booking.objects.filter(email = request.user.email).order_by('date', 'time') 

    # Variable containing all bookings associated with the customer_name used
    bookings_from_user_name = Booking.objects.filter(customer_name = request.user).order_by('date', 'time') # from user_name

    # If bookings_from_emails exists then they are the bookings
    if bookings_from_emails:
        bookings = bookings_from_emails
    else:
        # Otherwise  bookings_from_user_name are the bookings
        bookings = bookings_from_user_name

    context = {
        'bookings' : bookings
    }

    # Renders the view bookings page with the desired context
    return render(request, 'manage_bookings/view_bookings.html', context )



def edit_bookings(request, booking_id):
    """
    Function to render the edit bookings page and handle the form.
    """

    # Gets the required booking 
    booking = get_object_or_404(Booking, pk = booking_id)
   
    if request.method == 'POST':
        form = BookingForm(request.POST, instance = booking)

        # Create some variables from booking instance
        old_requested_date = getattr(booking, 'date')
        old_requested_time = getattr(booking, 'time')
        old_requested_guests = getattr(booking, 'number_of_guests')

        if form.is_valid():
            form_instance = form.save(commit=False)

            # Populate the booking instance customer_name field
            form_instance.customer_name = request.user

            # Populate the booking instance email field
            form_instance.email = request.user.email

            # Create some variables from the form displayed fields
            requested_date = booking.date
            requested_time = booking.time
            requested_guests = booking.number_of_guests

           

            # Checks if at least one on the fields has been edited
            if requested_date == old_requested_date and requested_time == old_requested_time and requested_guests == old_requested_guests:
                message = f"Your booking has no changes applied"
                messages.success(request, message)
            else:
            
                # List of tables from the BOOKING MODEL already assigned to requested time/date
                booked_tables = get_booked_tables(requested_date, requested_time)
                
                # List of tables in the TABLE MODEL excluding the tables assigned in BOOKING MODEL at requested time/date
                available_tables = Table.objects.exclude(pk__in = [table.pk for table in booked_tables])

                # Checks if there is at least one table available
                if available_tables.count() <= 0:
                    message = f"Unfortunately we fully booked at {requested_time} on {requested_date}."
                    messages.success(request, message)
                
                else:
                    # Calls the assign_table function to choose the most efficient table for the number of guests
                    form_instance.table = assign_table(available_tables, requested_guests)
                    form_instance.save()

                    message = f"Your booking has been changed to the {requested_date} at {requested_time} for {requested_guests} guest(s)."
                    messages.success(request, message)


        else:
            form = BookingForm()
            context = {'form': form}



            return render(request, 'manage_bookings/edit_bookings.html', context)
    else:
        form = BookingForm(instance = booking)
    
    context = {'form': form}
    return render(request, "manage_bookings/edit_bookings.html", context)


def cancel_bookings(request, booking_id):
    booking = get_object_or_404(Booking, pk = booking_id)
    if request.method == 'POST':
        form = CancelBookingForm(request.POST, instance = booking)

        # Create variables from booking instance
        requested_date = getattr(booking, 'date')
        requested_time = getattr(booking, 'time')
        requested_guests = getattr(booking, 'number_of_guests')

        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.customer_name = request.user

            form_instance.delete()
            #return redirect('view_bookings')  # Redirect to the view booking page to clear when instance is deleted

            message = f"Your booking on the {requested_date} at {requested_time} for {requested_guests} guest(s) has been canceled."
            messages.success(request, message)
            
        """  
        else:
            form = CancelBookingForm()
            context = {'form': form}
            return render(request, 'manage_bookings/cancel_bookings.html', context)
        """
        
    else:
        form = CancelBookingForm(instance = booking)
    
    context = {'form': form}
    return render(request, "manage_bookings/cancel_bookings.html", context)





    







