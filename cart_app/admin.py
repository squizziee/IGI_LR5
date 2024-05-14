from django.contrib import admin

from cart_app.models import Order, OrderEntry

admin.site.register(Order)
admin.site.register(OrderEntry)
