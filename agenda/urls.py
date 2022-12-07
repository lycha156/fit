from django.urls import path
from agenda import views

urlpatterns = [
    # AGENDA
    path('', views.index, name="agenda_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    path('create/turno', views.create_turno, name="agenda_create_turno"),
    path('create/evento', views.create_evento, name="agenda_create_evento"),
    # path('update/<int:id>', views.update, name="documentos_update"),
    # path('show/<int:id>', views.show, name="socios_show"),
    # path('delete/<int:id>', views.delete, name="documentos_delete"),
]