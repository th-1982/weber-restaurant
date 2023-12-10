from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Reservations
import datetime
from django.urls import reverse

# Create your tests here.
"""
In this test file I will divide the tests into different classes
instead of having all tests in one class for learning purposes
"""


class BaseTest(TestCase):
    """
    The purpose of this class is to reduce code duplication by 
    providing a common setup that can be inherited by multiple test classes.

    The class creates two users, one staff user and one non-staff user.
    It also creates two tables and one reservation.

    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='Mr McSchmoff',
            password='BuzzLightyearIsSexxi'
        )

        self.staff_user = User.objects.create_user(
            username='Ms Doubtfire',
            password='HelloDear',
            is_staff=True
        )

        self.table1 = Table.objects.create(table_number=1, capacity=4)
        self.table2 = Table.objects.create(table_number=2, capacity=4)

        Reservations.objects.create(
            user=self.user,
            table=self.table1,
            name='Spanky McSpankerson',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
            customer_email='mcspank2003@hotmail.com'
        )


class TestHomeView(TestCase):
    """
    Tests the home view for correct status code, template, and content.

    """

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertContains(response, 'Home')


class TestMenuView(TestCase):
    """
    Tests the menu view for correct status code, template, and content.
    """

    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertContains(response, 'Menu')



class TestCreateReservationView(BaseTest):
    """
    Test suite for the Create Reservation View.

    Tests goes over:
    - View accessibility and template usage.
    - Reservation creation functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A new reservation can be successfully created.
    """


    def test_create_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_create_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.post('/booking/', {
            'table': self.table2,
            'name': 'Tree Hugger',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 1,
            'number_of_guests': 2,
            'customer_email': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reservations.objects.count(), 1)

class TestUpdateReservationView(BaseTest):
    """
    Test for the update reservation view.

    Tests goes over:
    - View accessibility and template usage.
    - Reservation update functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A reservation can be successfully updated.

    """

    def test_update_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get('/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_edit.html')

    def test_update_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.post('/1/edit/', {
            'table': self.table1,
            'name': 'Spanky McSpankerson',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 2,  # Update time from 1 to 2
            'number_of_guests': 4,  # Update number_of_guests from 2 to 4
            'customer_email': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reservations.objects.get(id=1).time, 1)
        self.assertEqual(Reservations.objects.get(id=1).number_of_guests, 2)


class TestDeleteReservationView(BaseTest):
    """
    Test for the delete reservation view.
    
    Tests goes over:
    - View accessibility and template usage.
    - Reservation deletion functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A reservation can be successfully deleted.
    
    """

    def setUp(self):
        super().setUp()
        self.reservation = Reservations.objects.create(
            user=self.user,
            table=self.table1,
            name='Delete Me',
            date=datetime.date.today() + datetime.timedelta(days=3),
            time=2,
            number_of_guests=3,
        )
        self.delete_url = reverse(
            'reservation_delete', args=[self.reservation.id])

    def test_delete_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_delete.html')

    def test_authorized_user_delete_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'reservation_list'), fetch_redirect_response=False)
        # Verify the reservation was actually deleted
        with self.assertRaises(Reservations.DoesNotExist):
            Reservations.objects.get(id=self.reservation.id)