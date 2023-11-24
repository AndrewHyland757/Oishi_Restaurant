from django.shortcuts import render
from .forms import BookingForm

def home(request):
    #return render(request, "basic.html")
    
    form = BookingForm()
    context = { 'form' : form }
    
    return render(request, "index.html", context)
