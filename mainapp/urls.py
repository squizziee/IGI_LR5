from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('faq/', views.faqs),
    path('coupons/', views.coupons),
    path('privacy_policy/', views.privacy_policy),
    path('review/', views.reviews),
    path('review/add', views.add_review, name="add_review")
]
