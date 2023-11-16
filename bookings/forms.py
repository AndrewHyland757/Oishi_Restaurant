from django import forms
from .models import Reservation, Customer
from allauth.account.forms import LoginForm
#from allauth.account.forms import LogoutForm






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
        

class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        #self.fields['remember'].widget = forms.BooleanField(attrs={'class': 'form-control'})



      




class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields =  ['first_name', 'last_name', 'email', 'phone', 'password']
        
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms. PasswordInput(attrs={'class': 'form-control'}),
        }