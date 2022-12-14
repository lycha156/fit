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
    context = {}

    # al ingresar a show para la rutina. si la rutina NO existe, crea una nueva
    # de lo contrario, continua
    rutina = Rutina.objects.filter(socio = socio, agenda = agenda).first()
    if not rutina:
        Rutina.objects.create(socio = socio, agenda = agenda)
    else:
        series = Contenedor.objects.filter(rutina = rutina)
        context.update({'series': series})
        print(series)

    context.update({'rutina': rutina})
    return render(request, 'rutinas_show.html', context)

# SERIES

def series_create(request):
    rutina_id = request.POST.get('rutina_id')
    serie = request.POST.get('serie')
    rutina = get_object_or_404(Rutina, pk = rutina_id)

    if request.method == 'POST':
        try:
            instancia = Contenedor.objects.create(contenedor = serie, rutina = rutina)
            messages.success(request, f'Serie {instancia.contenedor} cargada con exito')
            return redirect('rutinas_show', rutina.socio.id, rutina.agenda.id)
        except Exception as e:
            messages.warning(request, f'Error durante la carga de datos. Error: {e}')
            return redirect('rutinas_show', rutina.socio.id, rutina.agenda.id)
    else:
        return redirect('rutinas_show', rutina.socio.id, rutina.agenda.id)
    
def series_delete(request, id):
    serie = get_object_or_404(Contenedor, pk=id)
    if request.method == 'POST':
        try:
            instancia = serie.delete()
            messages.success(request, f'Serie {instancia.contenedor} eliminada con exito.-')
            return redirect('series_delete')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos de la serie {instancia.container}, posee registros relacionados. Error: {e}')
            return redirect('series_delete')
    context = {
        'serie': serie
    }
    return render(request, 'series/series_delete.html', context)


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

