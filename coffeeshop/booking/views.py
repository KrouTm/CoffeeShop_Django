from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail

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
        message = '''
        New message: {}

        From: {}
        '''.format(data['comments'], data['email'])
        send_mail(data['nperson'], comments, '', ['c0e5a668ec9fc5'])

        return redirect('booking_success')
    else:
        return render(request, 'booking/booking.html')

def booking_success(request):
    return render(request, 'booking/booking_success.html')