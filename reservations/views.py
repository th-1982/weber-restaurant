from django.shortcuts import render



# Create your views here.


def homepage_view(request):
    return render(request, "reservations/homepage.html")

def contact_view(request):
    return render(request, "reservations/contact.html")

def menu_view(request):
    return render(request, "reservations/menu.html")

def booking_view(request):
    return render(request, "reservations/booking.html")