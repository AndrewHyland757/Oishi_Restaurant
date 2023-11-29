from django.shortcuts import render, redirect, reverse, get_object_or_404
# from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.contrib import messages
from .forms import BookingForm, BookingFormNotLoggedIn



def get_max_tables():
    """ Returns max number of tables in restaurant """
    max_tables = len(Table.objects.all())

    return max_tables


def get_tables_booked(requested_time, requested_date):
    """ Returns number of tables booked on requested time and date """
    tables_booked = len(Booking.objects.filter(
        time=requested_time,
        date=requested_date))

    return tables_booked


def check_availability(requested_time, requested_date):

    # Max number of tables in restaurant 
    max_tables = len(Table.objects.all())

    # Number of tables booked on requested time and date 
    tables_booked = len(Booking.objects.filter(
        time=requested_time,
        date=requested_date))
    
    if tables_booked < max_tables:
        return "Table available"




"""
#@login_required(login_url='accounts/login')
def home(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form = BookingForm(request.POST)
                #customer = get_customer(request, User)
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('guests')
                
                # Returns number of tables booked on requested time and date
                tables_booked = get_tables_booked(requested_time, requested_date)

                # Returns max number of tables 
                max_tables = get_max_tables()

                if tables_booked < max_tables:
                    form.save()
                #else:
                #raise ValidationError("Sorry, we are fully booked at that time.")
                #form = BookingForm()
    else:
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)
            if form.is_valid():
                form = BookingForm(request.POST)
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('guests')
                
                # Returns number of tables booked on requested time and date
                tables_booked = get_tables_booked(requested_time, requested_date)

                # Returns max number of tables 
                max_tables = get_max_tables()

                if tables_booked < max_tables:
                    form.save()
                #else:
                #raise ValidationError("Sorry, we are fully booked at that time.")
                #form = BookingForm()


    form = BookingForm()
    context = {
        'form': form
    }
    
    return render(request, "index.html", context)

"""




def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.customer_name = request.user
                form_instance.save()
                return redirect('home')  # Redirect to the home page to clear the form
        else:
            form = BookingForm()
    else:
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.save()
                return redirect('home')  # Redirect to the home page to clear the form
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
        form = BookingForm(request.POST, instance = booking)
        
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.customer_name = request.user
            form_instance.delete()
            return redirect('view_bookings')  # Redirect to the home page to clear the form
        else:
            form = BookingForm()
            context = {'form': form}
            return render(request, 'manage_bookings/cancel_bookings.html', context)
    else:
        form = BookingForm(instance = booking)
    
    context = {'form': form}
    return render(request, "manage_bookings/cancel_bookings.html", context)







"""
    booking = get_object_or_404(Booking, pk = booking_id)
    context = {'booking': booking}
    booking.delete()
    
    
    return render(request, 'manage_bookings/cancel_bookings.html', context)  
"""