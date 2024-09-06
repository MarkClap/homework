# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_propietarios, name='list_propietarios'),
    path('add/', views.add_propietario, name='add_propietario'),
    path('vehiculos/', views.list_vehiculos, name='list_vehiculos'),
    path('vehiculos/add/', views.add_vehiculo, name='add_vehiculo'),
    path('registrar/', views.registrar_evento, name='registrar_evento'),
    path('listar/', views.listar_registros, name='listar_registros'),
    path('propietario/<int:propietario_id>/', views.list_propietario_vehiculos, name='list_propietario_vehiculos'),
]
