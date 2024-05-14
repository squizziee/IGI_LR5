from django.db import models

from service_app.models import *
from user_app.models import UserProfile


# Instance of order. Created by client, edited by master.
class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total = models.FloatField("Total price with all additions")
    application_date = models.DateField("Date of order creation")
    deadline_date = models.DateField("Deadline of order completion")


# Entry in order. One order can contain multiple entries.
class OrderEntry(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
