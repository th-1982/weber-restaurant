from django.shortcuts import render
from .forms import ReservationForm
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Reservations

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class MenuView(TemplateView):
    template_name = 'menu.html'

class BookingView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'booking.html'
    form_class = ReservationForm
    fields = ['user', 'customer_email','name', 'date', 'time', 'notes', 'number_of_guests', 'table']
    success_url = reverse_lazy('reservation_list')
    success_message = "Booking Successful"

    def form_valid(self, form):
        # Save the form
        if form.is_valid():
            form.save()
            
            
        
        return super().form_valid(form)

class Reservation_List_View(ListView):
    model = Reservations
    template_name = "reservation_list.html"


class Reservation_Edit_View(SuccessMessageMixin, UpdateView):
    model = Reservations
    template_name = "reservation_edit.html"
    fields = ['user', 'customer_email','name', 'date', 'time', 'notes', 'number_of_guests', 'table']
    success_url = reverse_lazy("reservation_list")
    success_message = "Reservation Updated Successful"


class Reservation_Delete_View(SuccessMessageMixin, DeleteView):
    model = Reservations
    template_name = "reservation_delete.html"
    success_url = reverse_lazy("reservation_list")
    success_message = "Reservation Deleted Successful"


    

