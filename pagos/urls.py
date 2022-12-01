from django.urls import path
from . import views

urlpatterns = [
    # PAGOS
    path('', views.index, name="pagos_index"),
    path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    # path('create', views.create, name="socios_create"),
    path('update/<int:id>', views.update, name="pagos_update"),
    # path('show/<int:id>', views.show, name="socios_show"),
    path('delete/<int:id>', views.delete, name="pagos_delete"),
    path('generar_cuotas', views.generar_cuotas, name="generar_cuotas"),
    path('marcar_pago/<int:id>', views.marcar_pago, name="marcar_pago"),
    path('nuevo_cargo/<int:id>', views.nuevo_cargo, name="pagos_nuevo_cargo"),
]