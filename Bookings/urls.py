from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name="home"),
    path('view_bookings', views.view_bookings, name="view_bookings"),
    path('edit_bookings/<int:booking_id>/', views.edit_bookings, name="edit_bookings"),
    path('cancel_bookings/<int:booking_id>/', views.cancel_bookings, name="cancel_bookings"),
]

