import matplotlib
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from cart_app.models import OrderEntry
from service_app.models import Service, Master, DeviceType, ServiceType

from matplotlib import pyplot as plt
matplotlib.use('Agg')


def is_superuser(user):
    return user.is_superuser


def services_ordered_by_popularity():
    services = Service.objects.all()
    result = {}
    for service in services:
        count = 0
        entries = OrderEntry.objects.all()
        for entry in entries:
            if entry.service.id == service.id:
                count += 1
        result[service.name] = count
    return dict(sorted(result.items(), reverse=True, key=lambda el: el[1]))


def most_profitable_master():
    masters = Master.objects.all()
    result = {}
    for master in masters:
        total = 0.0
        entries = OrderEntry.objects.filter(master=master)
        for entry in entries:
            total += entry.count_total()
        result[master.name] = total
    return dict(sorted(result.items(), reverse=True, key=lambda el: el[1]))


def most_popular_devices():
    device_types = DeviceType.objects.all()
    result = {}
    for device_type in device_types:
        count = 0
        entries = OrderEntry.objects.filter(device_type=device_type)
        for entry in entries:
            count += 1
        result[device_type.name] = count
    return dict(sorted(result.items(), reverse=True, key=lambda el: el[1]))


@user_passes_test(is_superuser)
@login_required
def non_graph_metrics(request):
    m1 = services_ordered_by_popularity()
    metric1 = {
        'name': 'Most popular services',
        'list': m1
    }

    m2 = most_profitable_master()
    metric2 = {
        'name': 'Most profitable masters',
        'list': m2
    }

    m3 = most_popular_devices()
    metric3 = {
        'name': 'Most popular devices',
        'list': m3
    }
    print(metric1)
    return render(request, 'metric_app/metrics.html', {'metric1': metric1, 'metric2': metric2, 'metric3': metric3})


def service_type_graph():
    service_types = ServiceType.objects.all()
    result = {}
    for service_type in service_types:
        count = 0
        entries = OrderEntry.objects.filter(service_type=service_type)
        for entry in entries:
            count += 1
        result[service_type.name] = count
    names = list(result.keys())
    values = list(result.values())
    plt.bar(names, values, color='blue', width=0.5)
    plt.xlabel("Service types")
    plt.ylabel("Order entries")
    plt.title("Service types by order entries")
    plt.savefig("./img/service_type_graph.png")
    return "./img/service_type_graph.png"


def master_graph():
    masters = Master.objects.all()
    result = {}
    for master in masters:
        count = 0
        entries = OrderEntry.objects.filter(master=master)
        for entry in entries:
            count += 1
        result[master.name] = count
    names = list(result.keys())
    values = list(result.values())
    plt.barh(names, values, color='blue', height=0.5)
    plt.xlabel("Masters")
    plt.ylabel("Order entries")
    plt.title("Masters by count of order entries")
    plt.savefig("./img/master_graph.png")
    return "./img/master_graph.png"


@user_passes_test(is_superuser)
@login_required
def graph_metrics(request):
    g1_data = service_type_graph()
    plt.clf()
    g2_data = master_graph()
    plt.clf()
    return render(request, 'metric_app/graphics.html')
