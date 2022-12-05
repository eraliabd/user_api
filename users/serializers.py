from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'age', 'gender', 'date_of_birth',
                  'phone_number', 'address', 'image', 'created')
