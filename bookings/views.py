from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm

# Create your views here.

    
def index(request):
    return render(request, 'bookings/index.html')




def index(request):
    form = ReserveTableForm()
    if request.method == "POST":
        form =  ReserveTableForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReserveTableForm() 
    
    context = {
        "form": form
    }
    return render(request, 'bookings/index.html', {"form" : form})




    


def register(request):
    return render(request, 'bookings/register.html')


def login(request):
    return render(request, 'bookings/login.html')