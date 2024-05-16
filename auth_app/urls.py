from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_page, name='auth_page'),
    path('logout/', views.log_out, name='log_out'),
]
