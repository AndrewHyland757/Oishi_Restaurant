from django import forms
from .models import Booking
from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm
#from allauth.account.forms import LogoutForm


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


class YourLoginForm(LoginForm):
    
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
       
        
        #for field_name, field in self.fields.items():
            #field.widget.attrs['class'] = 'form-control'
            #del field.widget.attrs['placeholder']
        #del self.fields["remember"]
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-control'})
        #self.fields['remember'].widget = forms.CheckboxInput(attrs=['disable'] = True)
        #self.fields["remember"].disabled = True
        
        #self.fields['remember'].widget.attrs['diasbale'] = True

"""

class CustomSignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control'})
        #self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
"""

class CustomSignupForm(SignupForm):
    #Phone = forms.CharField(max_length=20)
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder']
            del field.widget.attrs['placeholder']


class CancelBookingForm(forms.ModelForm):
    
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