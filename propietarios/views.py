# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Propietario, Vehiculo, Registro

def list_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietarios/list_propietarios.html', {'propietarios': propietarios})

def add_propietario(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number_depart = request.POST.get('number_depart')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        # Crear un nuevo propietario y guardarlo en la base de datos
        Propietario.objects.create(
            name=name,
            number_depart=number_depart,
            phone_number=phone_number,
            email=email
        )
        return redirect('list_propietarios')  # Redirige a la vista de lista después de guardar
    
    return render(request, 'propietarios/add_propietario.html')

def list_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/list_vehiculos.html', {'vehiculos': vehiculos})

def add_vehiculo(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')
        propietario_id = request.POST.get('propietario')
        
        propietario = get_object_or_404(Propietario, id=propietario_id)
        
        Vehiculo.objects.create(
            matricula=matricula,
            marca=marca,
            modelo=modelo,
            color=color,
            propietario=propietario
        )
        return redirect('list_vehiculos')
    
    propietarios = Propietario.objects.all()
    return render(request, 'vehiculos/add_vehiculo.html', {'propietarios': propietarios})

def list_propietario_vehiculos(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    vehiculos = propietario.vehiculos.all()
    return render(request, 'vehiculos/list_propietario_vehiculos.html', {'propietario': propietario, 'vehiculos': vehiculos})

from django.utils import timezone

def registrar_evento(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        evento = request.POST.get('evento')
        
        vehiculo = get_object_or_404(Vehiculo, matricula=matricula)
        propietario = vehiculo.propietario

        Registro.objects.create(
            vehiculo=vehiculo,
            propietario=propietario,
            evento=evento,
            fecha_hora=timezone.now()
        )
        return redirect('listar_registros')
    
    return render(request, 'registros/registrar_evento.html')

def listar_registros(request):
    registros = Registro.objects.all().order_by('-fecha_hora')
    return render(request, 'registros/listar_registros.html', {'registros': registros})