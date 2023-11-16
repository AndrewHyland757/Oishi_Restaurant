from django.urls import path
from .views import index

urlpatterns = [
   path('', index, name= 'home'),
   #path('register', register, name= 'register'),
   #path('login', login, name= 'login'),  
]