from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('enfermera_list/', views.ipses_list, name='enfermeras_list'),
    path('', views.ipses_view, name='enfermeras_view'),
    path('<int:pk>', views.ips_view, name='enfermera_view'),
    path('<int:pk>/detail/', views.ips_detail, name='enfermera_detail'),

]