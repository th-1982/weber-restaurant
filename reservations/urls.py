from django.urls import path
from .views import homepage_view, menu_view, booking_view, contact_view

urlpatterns = [
    # path('', reservation_view, name='reservation_form')
    path('', homepage_view, name='homepage'),
    path('contact/', contact_view, name='contact'),
    path('menu/', menu_view, name='menu'),
    path('booking/', booking_view, name='booking')
]
