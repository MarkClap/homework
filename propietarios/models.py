# models.py
from django.db import models
from django.utils import timezone

class Propietario(models.Model):
    name = models.CharField(max_length=100)
    number_depart = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')

class Registro(models.Model):
    VEHICLE_IN = 'IN'
    VEHICLE_OUT = 'OUT'
    EVENT_CHOICES = [
        (VEHICLE_IN, 'Entrada'),
        (VEHICLE_OUT, 'Salida'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='registros')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='registros')
    evento = models.CharField(max_length=3, choices=EVENT_CHOICES, default=VEHICLE_IN)
    fecha_hora = models.DateTimeField(default=timezone.now)