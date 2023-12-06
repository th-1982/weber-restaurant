from django import forms
from .models import Reservations

# Using model forms so that we make use of the model fields when creating the form
class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        model = Reservations
        fields = ('user', 'customer_email','name', 'date', 'time', 'notes', 'number_of_guests', 'table',)