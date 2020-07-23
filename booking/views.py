from django.shortcuts import render, redirect
from .models import bookingItem

# Create your views here.


def get_booking_list(request):
    BookingItems = bookingItem.objects.all()
    context = {
        'BookingItems': BookingItems
    }
    return render(request, 'booking/booking_list.html', context)


def add_booking(request):
    if request.method == 'POST':
        name = request.POST.get('booking_name')
        bookingItem.objects.create(name=name)

        return redirect('bookig_list')
    return render(request, 'booking/add_booking.html')
