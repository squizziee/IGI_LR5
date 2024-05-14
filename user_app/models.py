from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField("User contact phone number", max_length=20)
    name = models.CharField("User full name", max_length=100)
    address = models.CharField("User full address", max_length=200)
    passport_serial = models.CharField("User passport serial", max_length=50)
