import logging

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from cart_app.models import Order, OrderEntry

logger = logging.getLogger(__name__)


def is_not_master(user):
    return not user.groups.filter(name="masters").exists()


@user_passes_test(is_not_master)
@login_required
def order_list(request):
    user = request.user
    orders = Order.objects.filter(user_profile__user=user)
    context = []
    for order in orders:
        entries = OrderEntry.objects.filter(order_id=order.id)
        context.append({
            'order': order,
            'entries': entries
        })
    return render(request, 'client_app/order_list.html', {'orders': context})


@user_passes_test(is_not_master)
@login_required
def cancel_order(request):
    order_id = request.POST.get('order_id')
    orders = Order.objects.filter(id=order_id)
    for order in orders:
        entries = OrderEntry.objects.filter(order_id=order.id)
        for entry in entries:
            entry.status = "Cancelled"
            entry.save()
            logger.info(f"Order with id {order.id} successfully cancelled by client")
    return redirect('order_list')
