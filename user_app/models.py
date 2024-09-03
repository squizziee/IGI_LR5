from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    phone_number = models.CharField("User contact phone number", max_length=20)
    name = models.CharField("User full name", max_length=100)
    address = models.CharField("User full address", max_length=200)
    passport_serial = models.CharField("User passport serial", max_length=50)

    import pytz
    #TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    #timezone = models.CharField(max_length=32, choices=TIMEZONES)

    def __str__(self):
        return f"{self.name} - {self.passport_serial}"
