from django.contrib.auth.models import User
from django.db import models

from service_app.models import Service
from user_app.models import UserProfile


class FAQ(models.Model):
    question = models.TextField("Question")
    answer = models.TextField("Answer")
    date = models.DateField("Date of answer")

    def __str__(self):
        return self.question


class CompanyInfo(models.Model):
    description = models.TextField("Info about the company")


class Coupon(models.Model):
    discount = models.IntegerField("Discount in percent", default=15)
    is_active = models.BooleanField("Can be used?", default=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.service.name} - {self.discount}% discount"


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField("Rating from 1 to 5", default=4)
    text = models.TextField("Review text")

    def __str__(self):
        return f"{self.user_profile.name} - {self.rating} of 5"

