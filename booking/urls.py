from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]