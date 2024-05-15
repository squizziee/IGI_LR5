import datetime
import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart_app.models import Order, OrderEntry
from service_app.models import ServiceType, Service, DeviceType, Device, Master
from user_app.models import UserProfile


def _deserialize_entries(request):
    items = []
    count = 0
    try:
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
    except:
        return []
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
    items = []
    try:
        items = _deserialize_entries(request)
    except:
        pass
    return render(request, 'cart_app/cart_items.html', {'items': items, 'item_ids': []})


def cart_checkout(request):
    items = json.loads(request.POST.get('items').replace('\'', '"'))
    return render(request, 'cart_app/checkout.html', {'items': items})


def _count_total(entries):
    total = 0.0
    for entry in entries:
        total += entry.service.base_price_in_usd
    return total


def _auth_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    address = request.POST.get('address')
    passport_serial = request.POST.get('passport_serial')

    user_profile = UserProfile.objects.filter(passport_serial=passport_serial).first()
    if user_profile is None:
        new_user = User()
        new_user.email = email
        new_user.password = password
        new_user.username = name
        new_user.save()

        new_user_profile = UserProfile()
        new_user_profile.user = new_user
        new_user_profile.phone_number = phone_number
        new_user_profile.name = name
        new_user_profile.address = address
        new_user_profile.passport_serial = passport_serial
        new_user_profile.save()
        return new_user_profile
    return user_profile


def create_order(request):
    user_profile = _auth_user(request)
    items = _deserialize_entries(request)
    entries = []

    order = Order()
    order.user_profile = user_profile
    order.application_date = datetime.datetime.today()
    order.save()

    for item in items:
        entry = OrderEntry()
        entry.order_id = order
        entry.service_type = item['service_type']
        entry.service = item['service']
        entry.device_type = item['device_type']
        entry.device = item['device']
        entry.master = item['master']
        entries.append(entry)
        entry.save()
        print(entry.order_id)
    order.total = _count_total(entries)
    order.save()
    request.session['cart']['items'] = []
    request.session.modified = True
    return redirect('home')
