from django import forms
from .models import Booking
#from allauth.account.forms import LoginForm
#from allauth.account.forms import LogoutForm


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields =  ['guests', 'date', 'time',]
        labels = {
        'guests': 'Number of guests',
        'date': 'Date',
        'time': 'Time',
    }
    
        widgets={
            'guests': forms.Select(attrs={'class': 'form-control' }),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control' }),
        }


class BookingFormNotLoggedIn(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields =  ['guests', 'date', 'time', 'email', 'customer' ]
        labels = {
        'guests': 'Number of guests',
        'date': 'Date',
        'time': 'Time',
        'customer': 'Name',
        'email': 'Email',
    }
    
        widgets={
            'guests': forms.Select(attrs={'class': 'form-control' }),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control' }),
            'customer': forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
        }



"""

class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['remember'].widget = forms.BooleanField(attrs={'class': 'form-control'})



class ReserveTableForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields =  ['number_of_guests', 'requested_date', 'requested_time',]
        labels = {
        'requested_date': 'Date',
        'requested_time': 'Time',
    }
        widgets={
            'number_of_guests': forms.Select(attrs={'class': 'form-control' }),
            'requested_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'requested_time': forms.Select(attrs={'class': 'form-control' }),
        }

"""  