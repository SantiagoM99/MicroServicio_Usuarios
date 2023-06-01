from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('medicocreate/', views.medico_create, name='createMedico'),
    path('', views.medicos_view, name='medicos_view'),
    path('medicos_list/', views.medicos_list, name='medicos_list'),
]