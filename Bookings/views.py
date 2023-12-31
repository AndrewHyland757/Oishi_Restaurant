from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.http import HttpResponse
from django.contrib import messages
from .forms import BookingForm, BookingFormNotLoggedIn, CancelBookingForm
from django.utils import timezone
from datetime import datetime


def get_booked_tables(requested_date, requested_time):
    """
    Returns any tables in the BOOKING MODEL assigned to requested time/date
    """
    # Gets all the bookings from the Booking model with the same time/date as
    # the users requested time/date
    filtered_booking_data = Booking.objects.filter(
        time=requested_time, date=requested_date)

    # Defines a list from each table used the booked tables
    booked_tables = [booking.table for booking in filtered_booking_data]

    # Returns the booked tables
    return booked_tables


def booking_success_message(requested_date, requested_time, requested_guests):
    """
    Returns the message used if the booking is a success
    """
    if int(requested_guests) == 1:
        message = f"Your booking has been made on the {requested_date} at {requested_time} for {requested_guests} guest"
    else:
        message = f"Your booking has been made on the {requested_date} at {requested_time} for {requested_guests} guests"
    return message


def booking_successful_change_message(requested_date, requested_time, requested_guests):
    """
    Returns the message used if the booking is a success
    """
    if int(requested_guests) == 1:
        message = f"Your booking has been changed to the {requested_date} at {requested_time} for {requested_guests} guest"
    else:
        message = f"Your booking has been changed to the {requested_date} at {requested_time} for {requested_guests} guests"
    return message


def assign_table(request, available_tables, requested_guests):
    """
    This function takes the available tables at users requested time/date and
    assigns the best size tableaccording to the number of guests.
    The parameters "available_tables" and "requested_guests" will be defined
    in the home function.
    """
    # The available_tables are sorted according to their number of seats
    available_tables = sorted(
        available_tables, key=lambda table: int(table.table_seats))
    '''
    message = ""
    '''
    # Iterates through the available_tables starting with lowest seat number
    for table in available_tables:

        # If table has the same amount of seats as requested guests it is
        # the perfect fit and returned
        if int(table.table_seats) == int(requested_guests):
            return table

        # If the iterated table has one extra seat it's returned next
        elif int(table.table_seats) == sum([int(requested_guests), 1]):
            return table

        # If the iterated table has two extra seat it's returned next
        elif int(table.table_seats) == sum([int(requested_guests), 2]):
            return table

        # If the iterated table has three extra seat it's returned next
        elif int(table.table_seats) == sum([int(requested_guests), 3]):
            return table

        else:
            # If there will be more than three empty seats at a booking it is
            # deemed inefficient and error message displayed
            message = f"Unfortunately, we have no available table for {requested_guests} at required date and time"

    # Error message shown if a table is not returned from the loop
    messages.error(request, message)


def home(request):
    """
    Function to render the home page and handle the reservation form
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

                # Create variables from the form displayed fields
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('number_of_guests')

                print(type(request.POST.get('date')))
                '''
                requested_date_int = int(request.POST.get('date'))

                your_date = datetime(requested_date_int)

                formatted_requested_date = your_date.strftime("%d-%m-%Y")
                '''

                date_obj = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')

                # Format the datetime object to a string in dd-mm-yyyy format
                formatted_date_str = date_obj.strftime('%d-%m-%Y')

                # Checks if the date is valid
                if requested_date <= str(timezone.now().date()):
                    message = f"{requested_date} is in the past. Please choose a valid date and time"
                    messages.error(request, message)
                else:
                    # List of tables from the BOOKING MODEL already assigned to
                    # requested time/date
                    booked_tables = get_booked_tables(
                        requested_date, requested_time)

                    # List of tables in the TABLE MODEL excluding the tables
                    # assigned in BOOKING MODEL at requested time/date
                    available_tables = Table.objects.exclude(pk__in=[
                        table.pk for table in booked_tables])

                    # Checks if there is at least one table available
                    if available_tables.count() <= 0:

                        # If not, message is shown
                        message = f"Unfortunately we fully booked at {requested_time} on {requested_date}"
                        messages.error(request, message)
                    else:
                        # Calls the assign_table function to check if any available table is a fit
                        # and assign the most efficent one
                        assigned_table = assign_table(request, available_tables, requested_guests)

                        # If a suitable table is found
                        if assigned_table:

                            # Fills the booking field
                            form_instance.table = assigned_table

                            # Gets the success message
                            message = booking_success_message(formatted_date_str, requested_time, requested_guests)

                            # Displays success message
                            messages.success(request, message)

                            # Saves the instance
                            form_instance.save()

                            # Duplicates avoided. Page is prevented from
                            # refreshing by the HTMX script in
                            # the head section of base.html template
                            return redirect('home')

        else:
            form = BookingForm()

    else:
        # If the user is not logged in, the guest booking form will be used
        # which contains extra fields
        if request.method == 'POST':
            form = BookingFormNotLoggedIn(request.POST)
            if form.is_valid():
                form_instance = form.save(commit=False)

                # Create variables from the form displayed fields
                requested_date = request.POST.get('date')
                requested_time = request.POST.get('time')
                requested_guests = request.POST.get('number_of_guests')

                # Checks if the date is valid
                if requested_date <= str(timezone.now().date()):
                    message = f"{requested_date} is in the past. Please choose a valid date and time"
                    messages.error(request, message)
                else:

                    # Gets tables from the BOOKING MODEL already assigned to
                    # requested time/date
                    booked_tables = get_booked_tables(
                        requested_date, requested_time)

                    # Gets the tables in the TABLE MODEL excluding the tables
                    # assigned in BOOKING MODEL at requested time/date
                    available_tables = Table.objects.exclude(
                        pk__in=[table.pk for table in booked_tables])

                    # Checks if there is at least one table available
                    if available_tables.count() <= 0:
                        message = f"Unfortunately, we fully booked at {requested_time} on {requested_date}"
                        messages.error(request, message)

                    else:
                        # Calls the assign_table function to check if any available table is a fit
                        # and assign the most efficent one
                        assigned_table = assign_table(
                            request, available_tables, requested_guests)

                        # If a suitable table is found
                        if assigned_table:

                            # Fills the booking field
                            form_instance.table = assigned_table

                            # Gets the success message
                            message = booking_success_message(
                                requested_date, requested_time, requested_guests)

                            # Displays success message
                            messages.success(request, message)

                            # Saves the instance
                            form_instance.save()

                            # Duplicates avoided. Page is prevented from
                            # refreshing by the HTMX script in
                            # the head section of base.html template
                            return redirect('home')
        else:
            form = BookingFormNotLoggedIn()

    context = {
        'form': form
        }

    return render(request, 'index.html', context)


@login_required(login_url='account_login')
def view_bookings(request):
    """
    Gets the reservations from the logged in user based on their email or user
    name (incase the superuser has not an email)
    If bookings were made as a guest before the user registered an account,
    it gets these bookings by the matching the emails.
    """

    # Variable containing all bookings associated with the email used
    bookings_from_emails = Booking.objects.filter(
        email=request.user.email).order_by('date', 'time')

    # Variable containing all bookings associated with the customer_name used
    bookings_from_user_name = Booking.objects.filter(
        customer_name=request.user).order_by('date', 'time')

    # If bookings_from_emails exists then they are the bookings
    if bookings_from_emails:
        bookings = bookings_from_emails
    else:
        # Otherwise  bookings_from_user_name are the bookings
        bookings = bookings_from_user_name

    context = {
        'bookings': bookings
        }

    # Renders the view bookings page with the desired context
    return render(request, 'manage_bookings/view_bookings.html', context)


def edit_bookings(request, booking_id):
    """
    Function to render the edit bookings page and handle the form.
    """
    # Gets the required booking
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)

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

                # Show message
                message = f"You have made no changes to your booking"
                messages.warning(request, message)
            else:
                # Checks if the date is valid
                if str(requested_date) <= str(timezone.now().date()):
                    message = f"{requested_date} is in the past. Please choose a valid date and time"
                    messages.error(request, message)

                else:
                    # List of tables from the BOOKING MODEL already
                    # assigned to requested time/date
                    booked_tables = get_booked_tables(
                        requested_date, requested_time)

                    # List of tables in the TABLE MODEL excluding the tables
                    # assigned in BOOKING MODEL at requested time/date
                    available_tables = Table.objects.exclude(
                        pk__in=[table.pk for table in booked_tables])

                    # Checks if there is at least one table available
                    if available_tables.count() <= 0:

                        # Displays fully booked message
                        message = f"Unfortunately we fully booked at {requested_time} on {requested_date}"
                        messages.error(request, message)

                    else:
                        # Calls the assign_table function to check if any
                        # available table is a fit
                        # and assign the most efficent one
                        assigned_table = assign_table(
                            request, available_tables, requested_guests)

                        # If a suitable table is found
                        if assigned_table:

                            # Fills the booking field
                            form_instance.table = assigned_table

                            # Gets the success message
                            message = booking_successful_change_message(
                                requested_date, requested_time, requested_guests)

                            # Displays success message
                            messages.success(request, message)

                            # Saves the instance
                            form_instance.save()

                            # Duplicates avoided. Page is prevented from
                            # refreshing by the HTMX script in
                            # the head section of base.html template
                            return redirect('view_bookings')
    else:
        form = BookingForm(instance=booking)
    context = {
        'form': form
        }
    return render(request, "manage_bookings/edit_bookings.html", context)


def cancel_bookings(request, booking_id):
    """
    Function to render the cancel bookings page and handle the form.
    """
    # Retrieve the booking
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = CancelBookingForm(request.POST, instance=booking)

        # Create variables from booking instance
        requested_date = getattr(booking, 'date')
        requested_time = getattr(booking, 'time')
        requested_guests = getattr(booking, 'number_of_guests')

        if form.is_valid():
            form_instance = form.save(commit=False)

            # Deletes the edited instance
            form_instance.delete()

            messages.warning(request, "Your booking on has been canceled")
            return redirect("view_bookings")
    else:
        form = CancelBookingForm(instance=booking)
    context = {
        'form': form
        }
    return render(request, "manage_bookings/cancel_bookings.html", context)
