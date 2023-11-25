from django.shortcuts import render, redirect, reverse
# from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.contrib import messages
from .forms import BookingForm, BookingFormNotLoggedIn



def get_max_tables():
    """ Returns max number of tables """
    max_tables = len(Table.objects.all())

    return max_tables


def get_tables_booked(requested_time, requested_date):
    """ Returns number of tables booked on requested time and date """
    tables_booked = len(Booking.objects.filter(
        time=requested_time,
        date=requested_date))

    return tables_booked


def get_customer(request, User):
    """ Returns customer instance if User is logged in """
    customer_email = request.user.email
    customer = Customer.objects.filter(email=customer_email).first()

    return customer


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

# #@login_required(login_url='accounts/login')
# def home(request):
    
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = BookingForm(request.POST)
#             if form.is_valid():
#                 form_instance = form.save(commit=False)
#                 form_instance.customer = request.user
#                 form_instance.save()
#                 messages.success(request,"Booking success!")

                
                
#         else:
#             form = BookingForm()
#     else:
        
#         messages.error(request, 'you must be registered and loggedin to make a booking!')
#         login_url = reverse('account_login')
#         #return redirect(login_url)
        
#     form = BookingForm()    
#     context = {'form': form}
#     return render(request, "index.html", context)

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.customer = request.user
                form_instance.save()
                return redirect('home')  # Redirect to the home page to clear the form
        else:
            form = BookingForm()
    else:
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)
        else:
            form = BookingFormNotLoggedIn()

    context = {'form': form}
    return render(request, "index.html", context)







"""

    form = BookingForm()
    context = {
        'form': form
    }
"""
   
    