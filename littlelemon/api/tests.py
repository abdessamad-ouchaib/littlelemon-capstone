from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from restaurant.models import Menu, Booking
from datetime import datetime
import pytz


class MenuAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        Menu.objects.create(name='Greek Salad', price=12.99, menu_item_description='Fresh salad')
        Menu.objects.create(name='Bruschetta', price=7.50, menu_item_description='Toasted bread')

    def test_get_menu_list_unauthenticated(self):
        """GET /api/menu/ should be accessible without authentication"""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_menu_list_returns_all_items(self):
        """GET /api/menu/ should return all menu items"""
        response = self.client.get('/api/menu/')
        self.assertEqual(len(response.data), 2)

    def test_create_menu_item_authenticated(self):
        """POST /api/menu/ requires authentication and creates an item"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            'name': 'Lemon Dessert',
            'price': '5.00',
            'menu_item_description': 'Sweet lemon cake'
        }
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)

    def test_create_menu_item_unauthenticated(self):
        """POST /api/menu/ without auth should return 403"""
        data = {'name': 'Unauthorized Item', 'price': '9.99', 'menu_item_description': ''}
        response = self.client.post('/api/menu/', data, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_get_single_menu_item(self):
        """GET /api/menu/<pk>/ should return a single item"""
        item = Menu.objects.first()
        response = self.client.get(f'/api/menu/{item.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], item.name)

    def test_update_menu_item(self):
        """PUT /api/menu/<pk>/ updates a menu item"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        item = Menu.objects.first()
        data = {'name': 'Updated Salad', 'price': '14.99', 'menu_item_description': 'Updated'}
        response = self.client.put(f'/api/menu/{item.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, 'Updated Salad')

    def test_delete_menu_item(self):
        """DELETE /api/menu/<pk>/ removes a menu item"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        item = Menu.objects.first()
        response = self.client.delete(f'/api/menu/{item.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)


class BookingAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='bookinguser', password='bookpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_bookings_list(self):
        """GET /api/bookings/ returns empty list initially"""
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        """POST /api/bookings/ creates a new booking"""
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 3,
            'booking_date': '2024-08-15T19:00:00Z'
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_bookings_require_authentication(self):
        """GET /api/bookings/ without token should be forbidden"""
        self.client.credentials()  # Remove credentials
        response = self.client.get('/api/bookings/')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_delete_booking(self):
        """DELETE /api/bookings/<pk>/ removes a booking"""
        booking = Booking.objects.create(
            name='Test Guest',
            no_of_guests=2,
            booking_date=datetime(2024, 9, 1, 18, 0, tzinfo=pytz.UTC)
        )
        response = self.client.delete(f'/api/bookings/{booking.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)


class UserRegistrationTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        """POST /auth/users/ creates a new user"""
        data = {
            'username': 'newuser',
            'password': 'StrongPass123!',
            'email': 'newuser@example.com'
        }
        response = self.client.post('/auth/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_obtain_token(self):
        """POST /auth/token/login/ returns a token for valid credentials"""
        User.objects.create_user(username='tokenuser', password='testpass456')
        data = {'username': 'tokenuser', 'password': 'testpass456'}
        response = self.client.post('/auth/token/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)
