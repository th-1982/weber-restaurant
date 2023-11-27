from django.contrib import admin
from .models import Reservations, Table 

# Register your models here.

admin.site.register(Table)

@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'time', 'notes', 'number_of_guests']

