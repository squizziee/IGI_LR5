import logging

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from cart_app.models import Order, OrderEntry
from master_app.models import Component, ComponentType

logger = logging.getLogger(__name__)


def is_master(user):
    return user.groups.filter(name="masters").exists()


@login_required
@user_passes_test(is_master)
def master_orders(request):
    user = request.user
    wrapper = []
    order_entries = OrderEntry.objects.filter(master__user=user)
    for entry in order_entries:
        order = entry.order_id
        client = order.user_profile
        wrapper.append({
            'client': client,
            'entry': entry
        })
    # print(order_entries)
    # orders = OrderEntry.objects.filter(mas)
    return render(request, 'master_app/master_orders.html', {'entries': wrapper})


@login_required
@user_passes_test(is_master)
def accept_order(request):
    order_entry_id = request.POST.get('order_entry_id')

    entry = OrderEntry.objects.filter(id=order_entry_id).first()
    entry.status = "In progress"
    entry.save()
    logger.info(f"Order entry with id {order_entry_id} successfully accepted")
    return redirect('/master/')


@login_required
@user_passes_test(is_master)
def component_list(request):
    search_query = request.GET.get('search_query')
    search_result = []
    if search_query is not None:
        search_result = Component.objects.filter(name__contains=search_query).order_by('price_in_usd')

    entry_id = request.GET.get('entry_id')
    component_types = ComponentType.objects.all()
    categorized_components = []
    for c_type in component_types:
        components = Component.objects.filter(component_type_id=c_type)
        categorized_components.append({
            'component_type': c_type,
            'components': components
        })
    present_components = []
    try:
        present_components = OrderEntry.objects.filter(id=entry_id).first().additional_components.all()
    except:
        pass
    return render(request, 'master_app/component_list.html',
                  {
                      'categories': categorized_components,
                      'entry_id': entry_id,
                      'present_components': present_components,
                      'search_result': search_result
                  })


@login_required
@user_passes_test(is_master)
def add_component(request):
    component_id = request.POST.get('component_id')
    entry_id = request.POST.get('entry_id')

    entry = OrderEntry.objects.filter(id=entry_id).first()
    component = Component.objects.filter(id=component_id).first()
    entry.additional_components.add(component)
    entry.save()
    logger.info(f"Order entry with id {entry_id} successfully updated")
    return redirect('/master/')


@login_required
@user_passes_test(is_master)
def remove_component(request):
    component_id = request.POST.get('component_id')
    entry_id = request.POST.get('entry_id')

    entry = OrderEntry.objects.filter(id=entry_id).first()
    component = Component.objects.filter(id=component_id).first()
    entry.additional_components.remove(component)
    entry.save()
    logger.info(f"Order entry with id {entry_id} successfully updated")
    return redirect('/master/')


@login_required
@user_passes_test(is_master)
def finish_order(request):
    entry_id = request.POST.get('entry_id')
    entry = OrderEntry.objects.filter(id=entry_id).first()
    entry.status = "Ready"
    entry.save()
    logger.info(f"Order entry with id {entry_id} successfully finished")
    return redirect('/master/')


@login_required
@user_passes_test(is_master)
def search_components(request):
    query = request.GET.get('search_query')
    result = Component.objects.filter(name__contains="query")
    return

