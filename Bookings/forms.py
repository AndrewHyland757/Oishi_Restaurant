from django import forms
from .models import Booking
from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm
#from allauth.account.forms import LogoutForm


# Registered user reserve table form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =  ['number_of_guests', 'date', 'time',]
        labels = {
        'number_of_guests': 'Number of guests',
        'date': 'Date',
        'time': 'Time',
        }
        widgets={
            'number_of_guests': forms.Select(attrs={'class': 'form-control' }),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control' }),
        }


# Guest user reserve table form
class BookingFormNotLoggedIn(forms.ModelForm):
    class Meta:
        model = Booking
        fields =  ['number_of_guests', 'date', 'time', 'email', 'guest_name']
        labels = {
        'number_of_guests': 'Number of guests',
        'date': 'Date',
        'time': 'Time',
        'guest_name': 'Name',
        'email': 'Email',
        }
        widgets={
            'number_of_guests': forms.Select(attrs={'class': 'form-control' }),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control' }),
            'guest_name': forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
        }


# Custom allauth login form
class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-control'})
        #for field_name, field in self.fields.items():
            #field.widget.attrs['class'] = 'form-control'
            #del field.widget.attrs['placeholder']
        
        
# Custom allauth signup form
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder']
            del field.widget.attrs['placeholder']


# Cancel booking form
class CancelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =  ['number_of_guests', 'date', 'time',]
        labels = {
        'number_of_guests': 'Number of guests',
        'date': 'Date',
        'time': 'Time',
        }

        # Fields are changed to read only
        widgets={
            'number_of_guests': forms.TextInput(attrs={'readonly':'readonly', 'class': 'form-control'}),  # compared to the widgets on the Bookingform
            'date': forms.DateInput(attrs={'readonly':'readonly', 'type': 'date', 'class': 'form-control'}),
            'time': forms.TextInput(attrs={'readonly':'readonly', 'class': 'form-control' }),
        }



     