from django.contrib import admin

from .models import ServiceType, DeviceType, Device, Service, MasterSpeciality, Master

admin.site.register(ServiceType)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(Service)
admin.site.register(MasterSpeciality)
admin.site.register(Master)
