from django.test import TestCase
from .models import Menu, Booking
from datetime import datetime
import pytz


class MenuModelTest(TestCase):

    def test_menu_str_representation(self):
        """Menu __str__ should return 'name : price'"""
        item = Menu.objects.create(
            name='Greek Salad',
            price=12.99,
            menu_item_description='Fresh tomatoes, olives, feta cheese'
        )
        self.assertEqual(str(item), 'Greek Salad : 12.99')

    def test_menu_item_creation(self):
        """Menu item is correctly saved to the database"""
        item = Menu.objects.create(
            name='Bruschetta',
            price=7.50,
            menu_item_description='Toasted bread topped with tomatoes'
        )
        self.assertEqual(item.name, 'Bruschetta')
        self.assertEqual(float(item.price), 7.50)

    def test_menu_get_all(self):
        """All menu items are returned correctly"""
        Menu.objects.create(name='Lemon Dessert', price=5.00)
        Menu.objects.create(name='Grilled Fish', price=18.00)
        self.assertEqual(Menu.objects.count(), 2)


class BookingModelTest(TestCase):

    def test_booking_str_representation(self):
        """Booking __str__ should return the guest name"""
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date=datetime(2024, 5, 15, 19, 0, tzinfo=pytz.UTC)
        )
        self.assertEqual(str(booking), 'John Doe')

    def test_booking_creation(self):
        """Booking is correctly saved with all fields"""
        booking = Booking.objects.create(
            name='Alice Smith',
            no_of_guests=2,
            booking_date=datetime(2024, 6, 1, 20, 30, tzinfo=pytz.UTC)
        )
        self.assertEqual(booking.no_of_guests, 2)
        self.assertEqual(booking.name, 'Alice Smith')
