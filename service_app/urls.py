
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.service_types, name='services'),
    path('/<str:service_type_id>/', views.services_of_given_type),
    path('/<str:service_type_id>/<str:service_id>/', views.device_types),
    path('/<str:service_type_id>/<str:service_id>/<str:device_type_id>/', views.devices),
    path('/<str:service_type_id>/<str:service_id>/<str:device_type_id>/<str:device_id>/masters', views.masters)
]
