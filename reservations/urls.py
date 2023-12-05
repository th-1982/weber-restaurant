from django.urls import path
# from .views import homepage_view, menu_view, booking_view, contact_view
from .views import HomePageView, MenuView, BookingView, ContactView, Reservation_List_View, Reservation_Edit_View,  Reservation_Delete_View



urlpatterns = [
    # path('', reservation_view, name='reservation_form')
    path('', HomePageView.as_view(), name='homepage'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('reservation_list', Reservation_List_View.as_view(), name='reservation_list'),
    path('<int:pk>/edit/', Reservation_Edit_View.as_view(), name="reservation_edit"),
    path('<int:pk>/delete/', Reservation_Delete_View.as_view(), name="reservation_delete"),

]
