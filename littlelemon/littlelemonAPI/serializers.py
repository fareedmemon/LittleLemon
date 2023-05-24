from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        