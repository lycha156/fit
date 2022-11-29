from django.shortcuts import render

# SOCIOS
def index(request):
    return render(request, 'socios_index.html')


# CUOTAS
def cuotas_index(request):
    return render(request, 'cuotas_index.html')