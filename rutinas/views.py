from django.shortcuts import render, redirect, get_object_or_404
from .models import Rutina, Ejercicio, Elemento, Contenedor
from agenda.models import Agenda
from socios.models import Socio
import datetime
from .forms import EjercicioForm
from django.contrib import messages

# RUTINAS
def index(request):

    socio = Socio.objects.get(pk = 1)
    agenda = Agenda.objects.filter(fecha = datetime.date.today()).order_by('fecha')

    context = {
        'fecha_hoy': datetime.date.today(),
        'rutinas': {'socio': 'Mauricio'},
        'socio': socio,
        'agendas': agenda
    }
    return render(request, 'rutinas_index.html', context)

def show(request, id, agenda ):
    socio = Socio.objects.get(pk = id)
    agenda = Agenda.objects.get(pk = agenda )

    context = {
        'socio': socio,
        'agenda': agenda
    }
    return render(request, 'rutinas_show.html', context)

# SERIES

def series_create(request):
    return render(request, 'series/series_create.html')


# EJERCICIOS

def ejercicios_index(request):
    context = {}
    ejercicios = Ejercicio()

    if request.method == 'POST':
        query = request.POST.get('q')
        ejercicios = Ejercicio.objects.filter(ejercicio__icontains = query)
        context.update({'q': query})
    else:
        ejercicios = Ejercicio.objects.all()[:50]

    context.update({
        'ejercicios': ejercicios,
    })
    return render(request, 'ejercicios/ejercicios_index.html', context)

def ejercicios_create(request):
    form = EjercicioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos guardados con exito.-')
            return redirect('ejercicios_index') 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('ejercicios_index') 

    context = {
        'form': form
    }
    return render(request, 'ejercicios/ejercicios_create.html', context)

def ejercicios_update(request, id):
    obj = get_object_or_404(Ejercicio, pk=id)
    form = EjercicioForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('ejercicios_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('ejercicios_index')

    context = {
        'form': form
    }
    return render(request, 'ejercicios/ejercicios_create.html', context)

def ejercicios_delete(request, id):
    ejercicio = get_object_or_404(Ejercicio, pk=id)
    if request.method == 'POST':
        try:
            ejercicio.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('ejercicios_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('ejercicios_index')
    context = {
        'ejercicio': ejercicio
    }
    return render(request, 'ejercicios/ejercicios_delete.html', context)

