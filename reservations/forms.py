from django import forms
from .models import Reservations

# Using model forms so that we make use of the model fields when creating the form
class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        model = Reservations
        fields = ('name', 'customer_email', 'date', 'time', 'notes', 'number_of_guests', 'table')


class SearchReservationForm(forms.Form):
    """
    This form is for searching existing table reservations.
    Available in staff accounts only.

    Attributes:
        booking_email (EmailField): An email field for searching by booking email.
        booking_date (DateField): A date field for searching by booking date.

    The form includes these fields:
        - booking_email: The email address used for the reservation.
        - booking_date: The date of the reservation.

    Both fields are optional and can be used to filter reservations based on either or both criteria.

    The form uses custom widgets with specific attributes for better user experience:
        - 'autocomplete': turned off for both fields.
        - 'aria-label': for accessibility.
        - 'placeholder': to guide the user.
        - 'class': for styling.
    """
    booking_email = forms.EmailField(
        label='Search Booking Email',
        required=False,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'aria-label': 'Search Booking by Email',
                'placeholder': 'Search Booking Email',
                'class': 'form-control'
            }))
    booking_date = forms.DateField(
        label='Search Booking Date',
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'autocomplete': 'off',
                'aria-label': 'Search Bookings by date',
                'placeholder': 'Search Booking Date',
                }))