"""restaurant_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.get_booking_list, kwargs=None, name='get_booking_list'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('edit/<bookingItem_id>', views.edit_booking, name='edit_booking'),
    path('delete/<bookingItem_id>',
         views.delete_booking, name='delete_booking'),
]
