from django import forms
from .models import Booking
from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm


class BookingForm(forms.ModelForm):
    """
    This form is used for registed users to make a booking.
    It takes the Booking model as its model and renders the
    time, guest and date fields. The email and customer name
    fields in the Booking model will be taken from the logged in user.
    """
    class Meta:

        model = Booking
        fields = ['number_of_guests', 'date', 'time']
        labels = {
            'number_of_guests': 'Number of guests',
            'date': 'Date',
            'time': 'Time',
        }

        # Widgets to add the 'form-control' class to each field
        widgets = {
            'number_of_guests': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
        }


class BookingFormNotLoggedIn(forms.ModelForm):
    """
    This form is used for non-registed users to make a booking.
    It also takes the Booking model as its model but renders the email
    and  guest name fields as inputs as well as the time, guest and date fields
    """
    class Meta:
        model = Booking
        fields = ['number_of_guests', 'date', 'time', 'email', 'guest_name']
        labels = {
            'number_of_guests': 'Number of guests',
            'date': 'Date',
            'time': 'Time',
            'guest_name': 'Name',
            'email': 'Email',
        }

        # 'form-control' class to each field displayed and set input type
        widgets = {
            'number_of_guests': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class YourLoginForm(LoginForm):
    """
    This form customises the allauth Login form
    """
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)

        # The 'form-control' class is added to each field
        # The remember field is not included
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control'})


class CustomSignupForm(SignupForm):
    """
    This form customises the allauth Signup form.
    """
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        # As the fields are looped;'form-control' class
        # is added and placeholder deleted
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder']
            del field.widget.attrs['placeholder']


class CancelBookingForm(forms.ModelForm):
    """
    This form handles booking cancelations displaying the number of
    guests, date and time fields of the booking as read-only fields.
    """
    class Meta:
        model = Booking
        fields = ['number_of_guests', 'date', 'time']
        labels = {
                'number_of_guests': 'Number of guests',
                'date': 'Date',
                'time': 'Time',
        }

        # Form-control and disable-hover class added each form field.
        # Attribute readonly is applied so that the form data can't be edited.
        widgets = {
            'number_of_guests': forms.TextInput(attrs={
                    'readonly': 'readonly', 'class':
                    'form-control disable-hover'}),
            'date': forms.DateInput(attrs={
                'readonly': 'readonly', 'type': 'date',
                'class': 'form-control disable-hover'}),
            'time': forms.TextInput(attrs={
                    'readonly': 'readonly', 'class':
                    'form-control disable-hover'})}
                    