from django.shortcuts import render
# from .forms import ReservationForm
from django.views.generic import TemplateView

# Create your views here.

# View to display the reservation form
# def reservation_view(request):
#     if request.method == "POST":
#         form = ReservationForm(request.POST)
#         if form.is_valid(): # Check if the form is valid
#             form.save()
#     else:
#         form = ReservationForm()
#     return render(request, "index.html", {"form":form})

class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class MenuView(TemplateView):
    template_name = 'menu.html'

class BookingView(TemplateView):
    template_name = 'booking.html'