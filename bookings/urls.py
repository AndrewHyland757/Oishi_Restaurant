from django.urls import path
from .views import index, register, login

urlpatterns = [
   path('', index, name= 'home'),
   path('register', register, name= 'register'),
   path('login', login, name= 'login'),
]