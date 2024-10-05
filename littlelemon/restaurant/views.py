from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework import generics
from rest_framework import viewsets
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

class MenuItemView(generics.ListCreateAPIView):
    """
    View to list all menu items and create a new menu item.
    Handles GET and POST method calls.
    """
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()  # Specify the queryset for menu items
    serializer_class = MenuSerializer  # Specify the serializer to use


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific menu item.
    Handles GET, PUT, and DELETE method calls.
    """
    queryset = Menu.objects.all()  # Specify the queryset for menu items
    serializer_class = MenuSerializer  # Specify the serializer to use

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer