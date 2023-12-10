from django.shortcuts import render
from .forms import ReservationForm, SearchReservationForm
import datetime
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
    context_object_name = 'reservations'

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
            booking_email = self.request.GET.get('booking_email')
            booking_date = self.request.GET.get('booking_date')

            if booking_email:  # If booking_email is not None
                queryset = queryset.filter(customer_email=booking_email)

            if booking_date:
                queryset = queryset.filter(date=booking_date)

            queryset = queryset.filter(
                date__gte=datetime.date.today()-datetime.timedelta(days=1))

            # If user is staff, return all reservations from today onwards
            return queryset

        else:
            # If user is not staff, return only reservations made by user
            return Reservations.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchReservationForm(
            self .request.GET or None)
        context['navbar'] = 'view'
        return context
        
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


    

