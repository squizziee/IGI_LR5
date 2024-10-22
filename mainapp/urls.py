from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('faq/', views.faqs, name='faq'),
    path('faq/<str:faq_id>', views.faq_page),
    path('coupons/', views.coupons, name='coupons'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('review/', views.reviews, name='reviews'),
    path('review/add', views.add_review, name="add_review"),

    path('table/', views.get_table_data, name="table"),
    path('masters/<int:master_id>', views.get_master_json, name="get_master"),
    path('masters/add', views.add_master, name="add_master"),
    path('oop/', views.oop_page, name="table"),
]
