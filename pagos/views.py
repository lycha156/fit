from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from socios.models import Socio, Cuota
from .models import Pago
from .forms import PagoForm
import datetime
from django.db.models import Q

def index(request):
    MESES = [
        {'id': 0, 'valor': '-Todos-'},
        {'id': 1, 'valor': '(1) Enero'},
        {'id': 2, 'valor': '(2) Febrero'},
        {'id': 3, 'valor': '(3) Marzo'},
        {'id': 4, 'valor': '(4) Abril'},
        {'id': 5, 'valor': '(5) Mayo'},
        {'id': 6, 'valor': '(6) Junio'},
        {'id': 7, 'valor': '(7) Julio'},
        {'id': 8, 'valor': '(8) Agosto'},
        {'id': 9, 'valor': '(9) Septiembre'},
        {'id': 10,'valor': '(10) Octubre'},
        {'id': 11,'valor': '(11) Noviembre'},
        {'id': 12,'valor': '(12) Diciembre'},
    ]

    ESTADOS = [
        {'id': "", 'valor': '-Todos-'},
        {'id': 'PAGO', 'valor': 'Pagos'},
        {'id': 'IMPAGO', 'valor': 'Impagos'}
    ]

    if request.method == 'POST':
        query = request.POST.get('q')
        mes = request.POST.get('mes')
        año = request.POST.get('año')
        estado = request.POST.get('estado')
        fecha = request.POST.get('fecha')
        pagos = Pago.objects.filter( Q(socio__nombre__icontains = query) | Q(socio__apellido__icontains = query) )
        if (mes != "0"):
            pagos = pagos.filter( mes = mes)
        if( año != ""):
            pagos = pagos.filter( año = año)
        if( estado != ""):
            pagos = pagos.filter( estado = estado)
        if( fecha != ""):
            pagos = pagos.filter(fechapago = fecha)

        context = {
            'pagos': pagos,
            'q': query,
            'meses': MESES,
            'mes': mes,
            'año': año,
            'estado': estado,
            'estados': ESTADOS,
            'fecha': fecha,
        }
        return render(request, 'pagos_index.html', context)

    else:
        pagos = Pago.objects.all()

    

    context = {
        'pagos': pagos,
        'meses': MESES,
        'estados': ESTADOS,
    }
    return render(request, 'pagos_index.html', context)

def generar_cuotas(request):
    if request.method == "POST":
        mes = request.POST.get('mes')
        año = request.POST.get('año')
        # check si las variables existen!
        socios = Socio.objects.filter(estado = 'ACTIVO')

        try:
            for socio in socios:
                pago = Pago()
                pago.socio = socio
                pago.mes = mes
                pago.año = año
                pago.estado = 'IMPAGO'
                pago.concepto = socio.cuota.concepto
                pago.monto = socio.cuota.monto
                pago.save()
            
            messages.success(request, f'Cuotas para el pediodo {mes}/{año}, generadas con exito.-')
            return redirect('pagos_index')
        except Exception as e:
            messages.warning(request, f'Error durante la generacion de las cuotas.- Error: {e}')
            return redirect('pagos_index')
        
def delete(request, id=id):
    pago = get_object_or_404(Pago, pk=id)
    if request.method == 'POST':
        try:
            pago.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('pagos_index')
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('pagos_index')
    context = {
        'pago': pago
    }
    return render(request, 'pagos_delete.html', context)

def update(request, id=id):
    obj = get_object_or_404(Pago, pk=id)
    form = PagoForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('pagos_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('pagos_index')

    context = {
        'form': form
    }
    return render(request, 'pagos_create.html', context)

def marcar_pago(request, id=id):
    pago = get_object_or_404(Pago, pk=id)
    pago.estado = "PAGO"
    pago.fechapago = datetime.date.today()
    try:
        pago.save()
        messages.success(request, 'Pago asentado con exito.-')
        return redirect('pagos_index')
    except Exception as e:
        messages.warning(request, f'Error al actualizar los datos. {e}')
        return redirect('pagos_index')

# busqueda de pagos asociados a socio
def pagos_socio(request, id=id):
    pagos = Pago.objects.filter(socio = id)
    context = {
        'pagos': pagos
    }
    return render(request, 'pagos_index.html', context)

# Nuevo cargo para socio especifico
def nuevo_cargo(request, id=id):
    socio = get_object_or_404(Socio, pk=id)
    form = PagoForm(request.POST or None)

    if form.is_valid():
        socio_id = request.POST.get('socio')
        try:
            instancia = form.save(commit=False)
            instancia.socio = Socio.objects.get(pk = socio_id)
            instancia.save()
            messages.success(request, 'Datos guardados con exito.-')
            return redirect('socios_show', socio_id) 
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('socios_show', socio_id) 

    context = {
        'socio': socio,
        'form': form
    }
    return render(request, 'pagos_create.html', context)
