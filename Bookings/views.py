from django.shortcuts import render, redirect, reverse, get_object_or_404
# from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.contrib import messages
from .forms import BookingForm, BookingFormNotLoggedIn, CancelBookingForm
from django.utils import timezone



def get_booked_tables(requested_date, requested_time):
    """
    Returns any tables assigned to requested time/date in the BOOKING MODEL 
    """
    #all_table_data = Booking.objects.values_list('table', flat=True)
    filtered_booking_data = Booking.objects.filter(time=requested_time,
        date=requested_date)

    booked_tables = [booking.table for booking in filtered_booking_data] # give the table form booking in each iteration of the loop
    
    return booked_tables




def get_tables():
    """
    Returns all tables from the TABLE MODEL
    """
    tables = Table.objects.all()
    return tables


def assign_table(available_tables, requested_guests):
    for table in available_tables:
        if int(table.table_seats) == int(requested_guests):
            #return [table]  # Perfect size
            return table
            
        elif int(table.table_seats) > int(requested_guests):
            #return [table]  # Table will have spare seats - that ok
            return table
        else:
            raise ValidationError("No available table for requested number of guests") # use alert from bootsrtap






def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.customer_name = request.user

                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('number_of_guests')

                #tables = get_tables() # list all tables in Table model
                booked_tables = get_booked_tables(requested_date, requested_time) # list of tables from BOOKING MODEL already assigned to requested time/date
               
                available_tables = Table.objects.exclude(pk__in = [table.pk for table in booked_tables])

                if available_tables.count() <= 0:
                    raise ValidationError("Already fully booked") # use alert from bootsrtap
                else:
                    form_instance.table = assign_table(available_tables, requested_guests)
                    #form_instance.table = tables.first()
                    #form_instance.table = available_tables.first()
                    #form_instance.table = available_tables.first()
                
                    form_instance.save()
                    return redirect('view_bookings')  # Redirect to the home page to clear the form      *** I indented these inwards ****
        else:
            form = BookingForm()
    else:
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.save()
                return redirect('view_bookings')  # Redirect to the home page to clear the form
        else:
            form = BookingFormNotLoggedIn()

    context = {'form': form}
    return render(request, "index.html", context)



@login_required(login_url='account_login')
def view_bookings(request):
    bookings = Booking.objects.filter(customer_name = request.user).order_by('date', 'time')
    context = {
        'bookings' : bookings
    }
    return render(request, 'manage_bookings/view_bookings.html', context )


def edit_bookings(request, booking_id):
    booking = get_object_or_404(Booking, pk = booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance = booking)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.customer_name = request.user
            form_instance.save()
            return redirect('view_bookings')  # Redirect to the home page to clear the form
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
        
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.customer_name = request.user
            form_instance.delete()
            return redirect('view_bookings')  # Redirect to the view booking page to clear when instance is deleted
        else:
            form = CancelBookingForm()
            context = {'form': form}
            return render(request, 'manage_bookings/cancel_bookings.html', context)
    else:
        form = CancelBookingForm(instance = booking)
    
    context = {'form': form}
    return render(request, "manage_bookings/cancel_bookings.html", context)





"""

def get_booking_date(pk):
    
    requested_date  = Booking.objects.filter(pk.requested_date)
        
    return requested_date


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():

            booking_details = form.cleaned_data # all the form data - from front end
            if booking_details ['date'] < timezone.now().date:
                raise ValidationError("Please choose a valid date") # use alert from bootsrtap
            
            overlapping_bookings = Booking.objects.filter(date= booking_details['date'], time= booking_details['time']).exclude(pk= booking_details.get("id", None)) # exclude this current forms instance
            if overlapping_bookings.exists():
                raise ValidationError("Already booked") # use alert from bootsrtap

"""
