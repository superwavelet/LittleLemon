from rest_framework import serializers
from .models import Menu  # Import the Menu model from your app's models
from .models import Booking
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'