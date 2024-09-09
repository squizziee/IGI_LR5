from django.urls import path

from vacancy_app import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancies')
]
