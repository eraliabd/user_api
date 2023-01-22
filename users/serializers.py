from rest_framework import serializers
from .models import User, Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'age', 'gender', 'date_of_birth',
                  'phone_number', 'address', 'image', 'created')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
