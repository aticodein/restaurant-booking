from django.shortcuts import render, redirect, get_object_or_404
from .models import bookingItem
from .forms import bookingItemForm

# Create your views here.


def get_booking_list(request):
    BookingItems = bookingItem.objects.all()
    context = {
        'BookingItems': BookingItems
    }
    return render(request, 'booking/booking_list.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = bookingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')

    form = bookingItemForm()
    context = {
        'form': form
    }
    return render(request, 'booking/add_booking.html', context)


def edit_booking(request, bookingItem_id):
    item = get_object_or_404(bookingItem, id=bookingItem_id)
    if request.method == 'POST':
        form = bookingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
    form = bookingItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


def delete_booking(request, bookingItem_id):
    item = get_object_or_404(bookingItem, id=bookingItem_id)
    item.delete()
    return redirect('get_booking_list')
