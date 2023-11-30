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
    Returns any tables in the Booking model assigned to requested time/date
    """
    #all_table_data = Booking.objects.values_list('table', flat=True)
    all_table_data = Booking.objects.values_list('table', flat=True)
    booked_tables = all_table_data.filter(
        time=requested_time,
        date=requested_date)
    
    return booked_tables


def get_available_tables(requested_date, requested_time):
    """
    Returns any tables in the Booking model available at requested time/date
    """
    #all_table_data = Booking.objects.values_list('table', flat=True)
    all_table_data = Booking.objects.values_list('table', flat=True)
    
    available_tables = all_table_data.exclude(
        time=requested_time,
        date=requested_date)
    
    return available_tables

def get_tables():
    """
    Returns all tables in Table model
    """
    tables = Table.objects.all()

    return tables


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

                tables = get_tables() # list all tables in Table model
                booked_tables = get_booked_tables(requested_date, requested_time) # list of tables in Booking model already assigned to requested time/date
                available_tables = get_available_tables(requested_date, requested_time)

                if len(booked_tables) == len(tables):
                    raise ValidationError("Already fully booked") # use alert from bootsrtap
                else:
                    form_instance.table = tables.first()
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
