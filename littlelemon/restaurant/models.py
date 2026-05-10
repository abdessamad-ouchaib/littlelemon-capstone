from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return f'{self.name} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
