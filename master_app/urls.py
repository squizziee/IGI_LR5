from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.master_orders, name='master_orders'),
    path('accept/', views.accept_order, name='accept_order'),
    path('finish/', views.finish_order, name='finish_order'),
    path('components/', views.component_list, name='component_list'),
    path('components/add', views.add_component, name='add_component'),
    path('components/remove', views.remove_component, name='remove_component'),
    path('components/search', views.search_components, name='search_components')
]
