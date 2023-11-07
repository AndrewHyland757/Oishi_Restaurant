from django.shortcuts import render
from .models import Reservation

# Create your views here.

    
def index(request):
    return render(request, 'bookings/index.html')


def register(request):
    return render(request, 'bookings/register.html')

def login(request):
    return render(request, 'bookings/login.html')