from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rutina, Ejercicio, Elemento, Contenedor, Rutina_modelo, Contenedor_modelo
from agenda.models import Agenda
from socios.models import Socio
import datetime
from .forms import EjercicioForm, ElementoForm, RutinaModeloForm, ContenedorModeloSerieForm, ElementoModeloForm
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
    
    if request.method == 'POST':
        query = request.POST.get('q')
        modelos_rutinas = Rutina_modelo.objects.filter(titulo__icontains = query)[:50]
    else:
        modelos_rutinas = Rutina_modelo.objects.all()[:50]

    context = {
        'form': form,
        'rutinas': modelos_rutinas
    }
    return render(request, 'rutinas_modelos/modelos_index.html', context)

def modelos_create(request):
    if request.method == 'POST':
        form = RutinaModeloForm(request.POST or None)

        if form.is_valid():
            try:
                instance = form.save()
                messages.success(request, f'Rutina {instance.titulo} creada con exito')
                return redirect('modelos_rutinas_index')
            except Exception as e:
                messages.warning(request, f'Error al crear la rutina {instance.titulo}. Error: {e}')
                return redirect('modelos_rutinas_index')
    else:
        return redirect('modelos_rutinas_index')

def modelos_update(request, id):
    obj = get_object_or_404(Rutina_modelo, pk=id)
    form = RutinaModeloForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('modelos_rutinas_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('modelos_rutinas_index')

    context = {
        'form': form
    }
    return render(request, 'rutinas_modelos/modelos_create.html', context)

def modelos_delete(request, id):

    rutina = get_object_or_404(Rutina_modelo, pk=id)
    if request.method == 'POST':
        try:
            rutina.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('modelos_rutinas_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('modelos_rutinas_index')
    context = {
        'rutina': rutina
    }
    return render(request, 'rutinas_modelos/modelos_delete.html', context)

def modelos_show(request, id):
    # rutina = Rutina_modelo.objects.get(pk = id).prefetch_related('contenedor_rutina_modelo')
    rutina = Rutina_modelo.objects.get(pk = id)
    series = Contenedor_modelo.objects.filter(rutina = rutina.id).prefetch_related('elemento_Contenedor_modelo')
    serieform = ContenedorModeloSerieForm(initial={'rutina': rutina.id})
    context = {
        'rutina': rutina,
        'form': serieform,
        'series': series
    }
    return render(request, 'rutinas_modelos/modelos_show.html', context)

# MODELOS SERIES

def modelos_series_create(request):
    if request.method == 'POST':
        form = ContenedorModeloSerieForm(request.POST or None)
        if form.is_valid():
            instancia = form.save()
            messages.success(request, f'La serie {instancia.contenedor}, fue guardada con exito.-')
            return redirect('modelos_rutinas_show', instancia.rutina.id)
        
    messages.warning(request, 'Error al cargar el formulario')
    return redirect('modelos_rutinas_index')

def modelos_series_update(request, id):
    obj = get_object_or_404(Contenedor_modelo, pk=id)
    form = ContenedorModeloSerieForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('modelos_rutinas_show', obj.rutina.id)
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('modelos_rutinas_show', obj.rutina.id)

    context = {
        'form': form
    }
    return render(request, 'rutinas_modelos/series/modelos_series_create.html', context)

def modelos_series_delete(request, id):
    serie = get_object_or_404(Contenedor_modelo, pk=id)

    if request.method == 'POST':
        try:
            rutina = Rutina_modelo.objects.get(pk = serie.rutina.id)
            serie.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('modelos_rutinas_show', rutina.id)
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('modelos_rutinas_show', rutina.id)
    context = {
        'serie': serie
    }
    return render(request, 'rutinas_modelos/series/modelos_series_delete.html', context)

# DETALLES DE LOS MODELOS DE LAS SERIES

def modelos_elementos_create(request, contenedor_id):
    contenedor = Contenedor_modelo.objects.get(pk = contenedor_id)
    form = ElementoModeloForm(request.POST or None, initial={'contenedor': contenedor})

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos guardados con exito.-')
            return redirect('modelos_rutinas_show', contenedor.rutina.id) 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('modelos_rutinas_show', contenedor.rutina.id) 

    context = {
        'form': form
    }
    return render(request, 'rutinas_modelos/elementos/modelos_elementos_create.html', context)