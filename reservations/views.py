from django.shortcuts import render



# Create your views here.


def homepage_view(request):
    return render(request, "homepage.html")

def contact_view(request):
    return render(request, "contact.html")

def menu_view(request):
    return render(request, "menu.html")

def booking_view(request):
    return render(request, "booking.html")