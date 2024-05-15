from django.db import models


class ComponentType(models.Model):
    name = models.CharField("Component name", max_length=150)
    description = models.CharField("Component description", max_length=200)

    def __str__(self):
        return self.name


class Component(models.Model):
    component_type_id = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    name = models.CharField("Component name", max_length=150)
    description = models.CharField("Component description", max_length=200)
    serial = models.CharField("Component serial number", max_length=50)
    price_in_usd = models.FloatField("Component price in USD", default=0)

    def __str__(self):
        return f"{self.name} - {self.serial}"
