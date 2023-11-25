from django.contrib import admin
from .models import Booking, Table
#from allauth.account.models import CustomUser

# Register your models here.

admin.site.register(Booking)
admin.site.register(Table)
#admin.site.register(CustomUser)

