from django.urls import path

from metric_app import views

urlpatterns = [
    path('', views.non_graph_metrics),
    path('graphics/', views.graph_metrics),
]
