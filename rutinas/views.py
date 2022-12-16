from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rutina, Ejercicio, Elemento, Contenedor
from agenda.models import Agenda
from socios.models import Socio
import datetime
from .forms import EjercicioForm, ElementoForm, RutinaModeloForm
from django.contrib import messages
from django.db.models import Q


# RUTINAS

def index(request):
    agenda = Agenda()
    context = {'fecha_hoy': datetime.date.today()}

    if request.method == 'POST':
        socio_query = request.POST.get('q')
        fecha_query = request.POST.get('fecha')
        
        # Si los filtros estan vacios, no pasa nada
        if socio_query == "" and fecha_query == "":
            return redirect('rutinas_index')

        # FILTRTADO
        agenda = Agenda.objects.all()

        if fecha_query != "":
            agenda = agenda.filter(fecha = fecha_query).order_by('-fecha')  

        if socio_query != "":
            agenda = agenda.filter( Q(socio__nombre__icontains = socio_query) | Q(socio__apellido__icontains = socio_query) ).order_by('-fecha')[:15]
        # FIN FILTRADO

        context.update({'fecha_hoy': datetime.datetime.strptime(fecha_query, '%Y-%m-%d').date()})
       
    else:
        agenda = Agenda.objects.filter(fecha = datetime.date.today()).order_by('-fecha')

    context.update({'agendas': agenda})

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

    rutina = Rutina.objects.filter(socio = socio, agenda = agenda).first()
    series = Contenedor.objects.filter(rutina = rutina).prefetch_related('elemento_contenedor')
    context.update({'series': series})

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
            nombre_serie_borrada = serie.contenedor
            rutina = Rutina.objects.get(pk = serie.rutina.id)
            instancia = serie.delete()
            messages.success(request, f'Serie {nombre_serie_borrada} eliminada con exito.-')
            return redirect('rutinas_show', rutina.socio.id, rutina.agenda.id)
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos de la serie {nombre_serie_borrada}, posee registros relacionados. Error: {e}')
            return redirect('rutinas_show', rutina.socio.id, rutina.agenda.id)
    context = {
        'serie': serie
    }
    return render(request, 'series/series_delete.html', context)


# DETALLS DE LA SERIE (ELEMENTOS)

def elementos_create(request, contenedor_id):
    contenedor = Contenedor.objects.get(pk = contenedor_id)
    form = ElementoForm(request.POST or None, initial={'contenedor': contenedor})

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos guardados con exito.-')
            return redirect('rutinas_show', contenedor.rutina.socio.id, contenedor.rutina.agenda.id) 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('rutinas_show', contenedor.rutina.socio.id, contenedor.rutina.agenda.id) 

    context = {
        'form': form
    }
    return render(request, 'elementos/elementos_create.html', context)

def elementos_update(request, id):
    obj = get_object_or_404(Elemento, pk=id)
    form = ElementoForm(request.POST or None, instance=obj)

    if form.is_valid():
        # contenedor = Contenedor.objects.get(pk = obj.contenedor.id)
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('rutinas_show', obj.contenedor.rutina.socio.id, obj.contenedor.rutina.agenda.id)
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('rutinas_show', obj.rutina.socio.id, obj.rutina.agenda.id)

    context = {
        'form': form
    }
    return render(request, 'elementos/elementos_create.html', context)

def elementos_delete(request, id):
    elemento = get_object_or_404(Elemento, pk=id)

    if request.method == 'POST':
        try:
            contenedor = Contenedor.objects.get(pk = elemento.contenedor.id)
            elemento.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('rutinas_show', contenedor.rutina.socio.id, contenedor.rutina.agenda.id)
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('rutinas_show', contenedor.rutina.socio.id, contenedor.rutina.agenda.id)
    context = {
        'elemento': elemento
    }
    return render(request, 'elementos/elementos_delete.html', context)


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
            # MEJOR ESTO, PARA QUE NO SE DE EL CASO DE BORRAR LAS FOTOS Y NO LA EL CAMPO
            ejercicio.foto.delete()
            ejercicio.video.delete()
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

def ejercicios_ajax(request):
    q = request.GET.get('search')
    data = []

    ejercicios = Ejercicio.objects.filter(ejercicio__icontains = q)
    for ejercicio in ejercicios:
        data.append({'id': ejercicio.id, 'text': ejercicio.ejercicio})

    return JsonResponse(data, safe=False)


# MODELOS RUTINAS

def modelos_index(request):
    form = RutinaModeloForm()

    context = {
        'form': form
    }
    return render(request, 'rutinas_modelos/modelos_index.html', context)