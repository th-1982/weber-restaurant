from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Provide a list of times for user reservation
RESERVATION_TIME = ((1, "12:00PM - 2:00PM"), (2, "2:00PM - 4:00PM"),
                    (3, "4:00PM - 6:00PM"), (4, "6:00PM - 8:00PM"),
                    (5, "8:00PM - 10:00PM"))

# Provides a list of choices when creating tables in our admin panel.
CAPACITY = ((2, "2"), (4, "4"), (6, "6"), (8, "8"))

class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=150)
    date = models.DateField()
    time = models.IntegerField(choices=RESERVATION_TIME, default=1)
    notes = models.TextField(null=True, blank=True) # This is not a required field
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY, default=2)

    def __str__(self):
        return str(self.table_number)

