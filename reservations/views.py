

from django.shortcuts import render
from .forms import ReservationForm, SearchReservationForm
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Reservations, Table
import datetime
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class MenuView(TemplateView):
    template_name = 'menu.html'


class BookingView(LoginRequiredMixin,  FormView):
    template_name = 'booking.html'
    form_class = ReservationForm
    fields = ['name', 'customer_email', 'date', 'time', 'notes', 'number_of_guests', 'table']
    success_url = reverse_lazy('reservation_list')
    model = Reservations

    def form_valid(self, form):
        """
        Before form submission, assign table with lowest capacity
        needed for booking guests
        """
        form.instance.customer = self.request.user
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        guests = form.cleaned_data['number_of_guests']
        # Filter tables with capacity greater or equal
        # to the number of guests
        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))
        # Get bookings on specified date
        bookings_on_requested_date = Reservations.objects.filter(
            date=date, time=time)
        # Iterate over bookings to get tables not booked
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.table.table_number:
                    tables_with_capacity.remove(table)
                    break
        # Iterate over tables not booked to get lowest
        # capacity table to assign to booking
        lowest_capacity_table = tables_with_capacity[0]
        for table in tables_with_capacity:
            if table.capacity < lowest_capacity_table.capacity:
                lowest_capacity_table = table
        form.instance.table = lowest_capacity_table

        messages.success(
            self.request,
            f'Booking confirmed for {guests} guests on {date}'
        )

        return super(BookingView, self).form_valid(form)

class Reservation_List_View(LoginRequiredMixin, ListView):
    model = Reservations
    template_name = "reservation_list.html"
    context_object_name = 'reservations'

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
            booking_email = self.request.GET.get('customer_email')
            booking_date = self.request.GET.get('date')

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


class Reservation_Edit_View(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Reservations
    template_name = "reservation_edit.html"
    fields = ['name', 'customer_email', 'date', 'time', 'notes', 'number_of_guests', 'table']
    success_url = reverse_lazy("reservation_list")
    model = Reservations

    def form_valid(self, form):
        """
        Before form submission, run capacity checks and
        assign to table with lowest capacity
        """
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        guests = form.cleaned_data['number_of_guests']

        # Filter tables with capacity greater or equal
        # to the number of guests
        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))
        # Get bookings on specified date
        bookings_on_requested_date = Reservations.objects.filter(
            date=date, time=time)
        # Iterate over bookings and remove table from bookings
        # with capacity
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.table.table_number:
                    tables_with_capacity.remove(table)
                    break
        # Iterate over tables with capacity and assign lowest
        # capacity table
        if tables_with_capacity:
            lowest_capacity_table = tables_with_capacity[0]
            for table in tables_with_capacity:
                if table.capacity < lowest_capacity_table.capacity:
                    lowest_capacity_table = table
            form.instance.table = lowest_capacity_table

        messages.success(
            self.request,
            f'Successfully updated booking for {guests} guests on {date}'
        )
        return super(Reservation_Edit_View, self).form_valid(form)

    def test_func(self):
        """ Test user is staff or throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


class Reservation_Delete_View(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservations
    template_name = "reservation_delete.html"
    success_url = reverse_lazy("reservation_list")
    success_message = "Deleted Successfully"

    def form_valid(self, form):
        """ Display toast message on form success """
        messages.success(
            self.request,
            'Successfully deleted booking'
        )
        return super(Reservation_Delete_View, self).form_valid(form)

    def test_func(self):
        """ Test user is staff else throw 403 """
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user