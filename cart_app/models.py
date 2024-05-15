import datetime

from django.db import models

from master_app.models import Component
from service_app.models import *
from user_app.models import UserProfile


# Instance of order. Created by client, edited by master.
class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total = models.FloatField("Total price with all additions", default=0)
    application_date = models.DateField("Date of order creation")
    deadline_date = models.DateField("Deadline of order completion", default=datetime.datetime.today() - datetime.timedelta(days=1))

    def __str__(self):
        return f"Order {self.id} by {self.user_profile.name}"

    def count_total(self):
        total = 0.0
        entries = OrderEntry.objects.filter(order_id=self.id)
        for entry in entries:
            total += entry.count_total()
        return total


# Entry in order. One order can contain multiple entries.
class OrderEntry(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    status = models.CharField("Order entry completion status", default="Awaiting acceptance", max_length=50)
    additional_components = models.ManyToManyField(Component)

    def __str__(self):
        return f"Order {self.order_id.id} - {self.service.name} - {self.status}"

    def count_total(self):
        total = 0.0
        for component in self.additional_components.all():
            total += component.price_in_usd
        return total + self.service.base_price_in_usd
