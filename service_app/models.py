from django.contrib.auth.models import User
from django.db import models


# Type of service for a client, e.g. Maintenance, Repairment, Upgrade, etc
class ServiceType(models.Model):
    name = models.CharField("Service type name", max_length=100)
    description = models.CharField("Service description", max_length=200)

    def __str__(self):
        return self.name


# Type of device available for service type, e.g. Stationary PC, Laptop, Smartphone, etc
class DeviceType(models.Model):
    name = models.CharField("Device type name", max_length=100)
    description = models.CharField("Device type description", max_length=200)

    def __str__(self):
        return self.name


# Instance of device. Won't be exact name, more like ASUS N550 series (as an example)
class Device(models.Model):
    name = models.CharField("Device name", max_length=200)
    serial = models.CharField("Serial number", max_length=200)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Service available for given service type, e.g. Repairment -> Liquid damage Repairment
class Service(models.Model):
    service_type_id = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    name = models.CharField("Service name", max_length=100)
    description = models.CharField("Service description", max_length=200)
    base_price_in_usd = models.FloatField("Base service price in USD without parts")
    device_types = models.ManyToManyField(DeviceType)

    def __str__(self):
        return self.name


# Master speciality, e.g. what kind of service master of certain speciality does
class MasterSpeciality(models.Model):
    name = models.CharField("Master speciality name", max_length=100)
    description = models.CharField("Master speciality description", max_length=200)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


# Master personal info
class Master(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Master name", max_length=100)
    experience_in_years = models.IntegerField("Work experience in years")
    speciality = models.ForeignKey(MasterSpeciality, on_delete=models.CASCADE)
    photo = models.ImageField('Profile picture for master', null=True)
    phone_number = models.CharField('Phone number', max_length=15, default="80291112233")

    def __str__(self):
        return self.name
