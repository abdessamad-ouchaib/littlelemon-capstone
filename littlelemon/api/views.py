from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


class MenuItemsView(generics.ListCreateAPIView):
    """
    GET  /api/menu/         – list all menu items (public)
    POST /api/menu/         – create a menu item (authenticated)
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/menu/<int:pk>/  – retrieve single item (public)
    PUT    /api/menu/<int:pk>/  – update item (authenticated)
    DELETE /api/menu/<int:pk>/  – delete item (authenticated)
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for table bookings.
    GET    /api/bookings/        – list bookings
    POST   /api/bookings/        – create booking
    GET    /api/bookings/<pk>/   – retrieve booking
    PUT    /api/bookings/<pk>/   – update booking
    DELETE /api/bookings/<pk>/   – delete booking
    All endpoints require authentication.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
