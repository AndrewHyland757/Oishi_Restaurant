from django import forms
from .models import Reservation



class ReserveTableForm(forms.ModelForm):
    
    
    class Meta:
        model = Reservation
        fields =  ['number_of_guests', 'requested_date', 'requested_time']
        labels = {
        'requested_date': 'Date',
        'requested_time': 'Time',
    }
        widgets={
            'number_of_guests': forms.Select(attrs={'class': 'form-control' }),
            'requested_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'requested_time': forms.Select(attrs={'class': 'form-control' }),
        }
        
