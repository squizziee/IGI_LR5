from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_method, name='news'),
    path('<str:article_id>', views.news_article_page)
]
