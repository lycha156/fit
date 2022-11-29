from django.shortcuts import render

def index(request):
    return render(request, 'pagos_index.html')

def generar_cuotas_mes(request):
    pass
