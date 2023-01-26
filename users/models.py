from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# from birthday import BirthdayField, BirthdayManager


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

    objects = UserManager()

    def validate_password(self, password):
        password_set = self.set_password(password)
        return password_set


class Person(models.Model):
    owner = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.owner

