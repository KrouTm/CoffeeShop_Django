from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from .models import Booking

def booking(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        nperson = request.POST.get('nperson')
        comments = request.POST.get('comments')

        booking = Booking(
            date=date,
            time=time,
            name=name,
            lastname=lastname,
            email=email,
            phone=phone,
            nperson=nperson,
            comments=comments
        )
        booking.save()

        data = {
            'date': date,
            'time': time,
            'name': name,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'nperson': nperson,
            'comments': comments
        }
        message = f'''
        You’re going fishing! View booking details within

        Date: {data['date']}
        Time: {data['time']}
        Name: {data['name']}
        Last Name: {data['lastname']}
        E-mail: {data['email']}
        Phone: {data['phone']}
        Guests: {data['nperson']}
        Comments: {data['comments']}
        '''
        send_mail(data['date'], message, '', ['c0e5a668ec9fc5'])



        return redirect('booking_success')
    else:
        return render(request, 'booking/booking.html')

def booking_success(request):
    return render(request, 'booking/booking_success.html')