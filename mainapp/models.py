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
    description = models.TextField("Info about the company in html")
    logo = models.ImageField("Company logo", null=True)
    promo_video = models.CharField("Promo video link", max_length=150, default="/")
    certificate = models.ImageField("Company certificate", null=True)
    requisite = models.TextField("Company requisites in html", default="")


class Coupon(models.Model):
    discount = models.IntegerField("Discount in percent", default=15)
    is_active = models.BooleanField("Can be used?", default=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    promocode = models.CharField("Promocode", max_length=100, default="")

    def __str__(self):
        return f"{self.service.name} - {self.discount}% discount - {self.promocode}"


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField("Rating from 1 to 5", default=4)
    text = models.TextField("Review text")
    created_at = models.DateTimeField(auto_now=True)
    speed_rating = models.IntegerField("Service speed rating from 1 to 5", default=4)
    is_pleasant_master = models.BooleanField("Was master pleasant to communicate with", default=False)
    is_clean_service = models.BooleanField("Was the job done clean", default=False)

    def __str__(self):
        return f"{self.user_profile.name} - {self.rating} of 5"


class CompanyPrivacyPolicy(models.Model):
    htmltext = models.TextField("Html for privacy policy")


class CompanySponsor(models.Model):
    name = models.CharField("Sponsor name", max_length=100)
    logo = models.ImageField("Sponsor logo", null=True)
    info = models.TextField("Sponsor additional info")
    website_link = models.CharField("Sponsor name", max_length=100, default="/")

    def __str__(self):
        return f"{self.name}"


class CompanyBanner(models.Model):
    image = models.ImageField("Banner image", null=True)
    description = models.TextField("Banner info")
