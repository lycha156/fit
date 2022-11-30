from django.shortcuts import render

def index(request):
    return render(request, 'pagos_index.html')

def generar_cuotas(request):
    return render(request, 'generar_cuotas.html')
