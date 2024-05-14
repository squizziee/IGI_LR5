from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('faq/', views.faqs),
    path('privacy_policy/', views.privacy_policy)
]
