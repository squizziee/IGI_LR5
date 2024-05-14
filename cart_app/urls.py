
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.cart_items, name='cart_items'),
    path('checkout/', views.cart_checkout, name='cart_checkout'),
    path('create_order/', views.create_order, name='create_order'),
]
