from django.urls import path

from client_app import views

urlpatterns = [
    path('', views.order_list, name="order_list"),
    path('cancel/', views.cancel_order, name="cancel_order"),
]
