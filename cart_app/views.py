import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from service_app.models import ServiceType, Service, DeviceType, Device, Master


def _deserialize_entries(request):
    items = []
    count = 0

    for entry in request.session['cart']['items']:
        service_type = ServiceType.objects.filter(id=entry['service_type']).first()
        service = Service.objects.filter(id=entry['service']).first()
        device_type = DeviceType.objects.filter(id=entry['device_type']).first()
        device = Device.objects.filter(id=entry['device']).first()
        master = Master.objects.filter(id=entry['master']).first()
        items.append({
            'service_type': service_type,
            'service': service,
            'device_type': device_type,
            'device': device,
            'master': master,
            'index': count
        })
        count += 1
    return items


def add_to_cart(request):
    if request.method == "POST":
        service_type_id = request.POST.get('service_type')
        service_id = request.POST.get('service')
        device_type_id = request.POST.get('device_type')
        device_id = request.POST.get('device')
        master_id = request.POST.get('master')
        full_entry = {
            'service_type': service_type_id,
            'service': service_id,
            'device_type': device_type_id,
            'device': device_id,
            'master': master_id
        }
        try:
            items = request.session['cart']['items']
            items.append(full_entry)
            request.session['cart']['items'] = items
        except:
            request.session['cart'] = {'items': []}
            items = request.session['cart']['items']
            items.append(full_entry)
            request.session['cart']['items'] = items
        # print(full_entry)
        # print(request.session['cart']['items'])
        request.session.modified = True
        return redirect(f'/services/{service_type_id}/{service_id}/{device_type_id}/{device_id}/masters')
    return redirect('/')


def remove_from_cart(request):
    index = int(request.POST.get('entry_index'))
    del request.session['cart']['items'][index]
    request.session.modified = True
    return redirect('/cart/')


def cart_items(request):
    items = _deserialize_entries(request)
    return render(request, 'cart_app/cart_items.html', {'items': items, 'item_ids': request.session['cart']['items']})


def cart_checkout(request):
    items = json.loads(request.POST.get('items').replace('\'', '"'))
    return render(request, 'cart_app/checkout.html', {'items': items})


def create_order(request):
    items = _deserialize_entries(request)
    pass
