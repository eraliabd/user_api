from django.db import models
from django.contrib.auth.models import AbstractUser
from birthday import BirthdayField, BirthdayManager


class User(AbstractUser):
    CHOOSE = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=10, choices=CHOOSE)
    image = models.ImageField(upload_to='users_images')
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = BirthdayManager()
