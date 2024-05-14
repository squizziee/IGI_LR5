from django.db.models import QuerySet
from django.shortcuts import render
from .models import *


def service_types(request):
    service_type_list = ServiceType.objects.all()
    return render(request, 'service_app/service_types.html', {'service_types': service_type_list})


def services_of_given_type(request, service_type_id):
    services = Service.objects.filter(service_type_id=service_type_id)
    return render(request, 'service_app/services.html', {'services': services})


def device_types(request, service_type_id, service_id):
    service = Service.objects.filter(id=service_id).first()
    device_type_list = list(service.device_types.all())
    return render(request, 'service_app/device_types.html', {'device_types': device_type_list})


def devices(request, service_type_id, service_id, device_type_id):
    device_list = Device.objects.filter(device_type_id=device_type_id)
    return render(request, 'service_app/devices.html', {'devices': device_list})


def masters(request, service_type_id, service_id, device_type_id, device_id):
    master_specialities = MasterSpeciality.objects.filter(services=service_id)
    master_list = []
    for spec in master_specialities:
        master_list += list(Master.objects.filter(speciality=spec.id))

    service_type = ServiceType.objects.filter(id=service_type_id).first()
    service = Service.objects.filter(id=service_id).first()

    device_type = DeviceType.objects.filter(id=device_type_id).first()
    device = Device.objects.filter(id=device_id).first()

    full_entry = {
        'service_type': service_type,
        'service': service,
        'device_type': device_type,
        'device': device,
        'master_list': master_list
    }
    return render(request, 'service_app/service_masters.html', full_entry)
