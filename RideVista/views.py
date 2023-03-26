from django.shortcuts import render, HttpResponseRedirect

from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail


def ride(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        number_of_travelers = request.POST.get('number_of_travelers', '')
        cab_type = request.POST.get('cab_type', '')

       
        to_location = request.POST.get('to_location', '')
        one_way_or_two_way = request.POST.get('one_way_or_two_way', '')
        pickup_location = request.POST.get('pickup_location', '')
        pickup_date = request.POST.get('pickup_date', '')
        return_date = request.POST.get('return_date', '')
        email = 'joydenver0@gmail.com'


        subject = f'New ride booking from{name}'

        message = f'''
        Name: {name}
        Phone: {phone}
        To Location: {to_location}
        One or Two way: {one_way_or_two_way}
        Pickup Location: {pickup_location}
        Number of travelers: {number_of_travelers}
        Cab Type: {cab_type}
        pickup_date: {pickup_date}
        Return date: {return_date}

        
        '''
        if subject and message:
            try:
                send_mail(subject, message, email, ['joydenver01@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/success/')
        else:
        # In reality we'd use a form class
        # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'RideVista/ride.html')

def success(request):
    return render(request, 'RideVista/response.html')


def home(request):
    return render(request, 'RideVista/index.html')



