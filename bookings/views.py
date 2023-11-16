from django.shortcuts import render
from .models import Reservation, Customer
from .forms import ReserveTableForm, CustomerForm

# Create your views here.

    
def index(request):
    return render(request, 'index.html')


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
    return render(request, 'index.html', {"form" : form})


#def login(request):
    #return render(request, '/login.html')

#def register(request):
    #return render(request, '/register.html')