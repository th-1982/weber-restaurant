from django.shortcuts import render
from .forms import ReservationForm
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class MenuView(TemplateView):
    template_name = 'menu.html'

class BookingView(FormView):
    template_name = 'booking.html'
    form_class = ReservationForm
    fields = ['user', 'customer_email','name', 'date', 'time', 'notes', 'number_of_guests', 'table']
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # Save the form
        form.save()
        return super().form_valid(form)