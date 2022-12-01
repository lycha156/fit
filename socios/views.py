from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cuota, Socio
from .forms import CuotaForm, SocioForm
from pagos.models import Pago
from django.db.models import Q

# SOCIOS
def index(request):
    socios = Socio.objects.all()
    context = {
        'socios': socios
    }
    return render(request, 'socios_index.html', context)

def create(request):
    form = SocioForm()
    if request.method == 'POST':
        form = SocioForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Datos del socio guardados con exito.')
                return redirect('socios_index')
            else:
                messages.warning(request, 'Error durante la carga de datos')
                return render(request, 'socios_create.html', context = {'form': form})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('socios_index')

    context = {
        'form': form,
    }
    return render(request, 'socios_create.html', context)

def update(request, id=id):
    obj = get_object_or_404(Socio, pk=id)
    form = SocioForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('socios_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('socios_index')

    context = {
        'form': form
    }
    return render(request, 'socios_create.html', context)

def delete(request, id=id):
    socio = get_object_or_404(Socio, pk=id)
    if request.method == 'POST':
        try:
            socio.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('socios_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del socio, posee registros relacionados. {e}')
            return redirect('socios_index')
    context = {
        'socio': socio
    }
    return render(request, 'socios_delete.html', context)

def show(request, id=id):
    socio = get_object_or_404(Socio, pk=id)
    pagos = Pago.objects.filter(socio = socio.id)[:5]
    if Pago.objects.filter( Q(socio = socio.id) and Q(estado = 'IMPAGO') ).count() == 0:
        aldia = 'Al Dia'
    else:
        aldia = 'Con Deuda'

    context = {
        'socio': socio,
        'pagos': pagos,
        'aldia': aldia
    }
    return render(request, 'socios_show.html', context)

# CUOTAS
def cuotas_index(request):
    cuotas = Cuota.objects.all()
    context = {
        'cuotas': cuotas
    }
    return render(request, 'cuotas_index.html', context)

def cuotas_create(request):
    form = CuotaForm()
    if request.method == 'POST':
        form = CuotaForm(request.POST)

        try:
            if form.is_valid():
                resultado = form.save()
                messages.success(request, 'Categoria de cuota creada con exito.')
                return redirect('cuotas_index')
            else:
                messages.warning(request, 'Error durante la carga de datos')
                return render(request, 'cuotas_create.html', context = {'form': form})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('cuotas_index')

    context = {
        'form': form,
    }
    return render(request, 'cuotas_create.html', context)

def cuotas_update(request, id=id):
    obj = get_object_or_404(Cuota, pk=id)
    form = CuotaForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('cuotas_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('cuotas_index')

    context = {
        'form': form
    }
    return render(request, 'cuotas_create.html', context)

def cuotas_delete(request, id=id):
    cuota = get_object_or_404(Cuota, pk=id)
    if request.method == 'POST':
        try:
            cuota.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('cuotas_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos de la cuota, posee registros relacionados. {e}')
            return redirect('cuotas_index')
    context = {
        'cuota': cuota
    }
    return render(request, 'cuotas_delete.html', context)