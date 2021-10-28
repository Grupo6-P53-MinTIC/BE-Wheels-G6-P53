from rest_framework import serializers
from authApp.models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['id', 'name', 'city', 'email', 'cellphone', 'date', 'is_manager']

