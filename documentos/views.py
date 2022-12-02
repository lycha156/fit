from django.shortcuts import render, redirect, get_object_or_404
from .models import Documento
from .forms import DocumentoForm
from django.contrib import messages
from socios.models import Socio

def create(request, id=id):
    socio = get_object_or_404(Socio, pk=id)
    socio_id = socio.id
    form = DocumentoForm()
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.socio = Socio.objects.get(pk=socio.id)
                instancia.save()
                messages.success(request, 'Documento cargado con exito')
                return redirect('socios_show', socio.id)
            else:
                messages.warning(request, 'Error durante la carga de datos')
                return render(request, 'documentos_create.html', context = {'form': form, 'socio': socio})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('socios_show', socio.id)

    context = {
        'form': form,
        'socio': socio,
        'socio_id': socio_id
    }
    return render(request, 'documentos_create.html', context)

def delete(request, id=id):
    documento = get_object_or_404(Documento, pk=id)
    if request.method == 'POST':
        socio_id = documento.socio.id
        try:
            documento.delete()
            messages.success(request, 'Datos eliminados con exito.-')
            return redirect('socios_show', socio_id)
        except Exception as e:
            messages.warning(request, f'No es posible eliminar los datos del pago, posee registros relacionados. {e}')
            return redirect('socios_show', socio_id)
    context = {
        'documento': documento
    }
    return render(request, 'documentos_delete.html', context)

def update(request, id=id):
    obj = get_object_or_404(Documento, pk=id)
    form = DocumentoForm(request.POST or None, request.FILES or None, instance=obj)
    socio_id = obj.socio.id
    if form.is_valid():
        try:
            instancia = form.save(commit=False)
            instancia.socio = Socio.objects.get(pk=socio_id)
            instancia.save()
            messages.success(request, 'Datos actualizados con exito.-')
            return redirect('socios_show', socio_id)
        except Exception as e:
            messages.warning(request, f'Error al actualizar los datos. {e}')
            return redirect('socios_show', socio_id)

    context = {
        'form': form,
        'socio_id': socio_id
    }
    return render(request, 'documentos_create.html', context)