from django.urls import path
from agenda import views

urlpatterns = [
    # AGENDA
    path('', views.index, name="agenda_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    # path('create/<int:id>', views.create, name="documentos_create"),
    # path('update/<int:id>', views.update, name="documentos_update"),
    # path('show/<int:id>', views.show, name="socios_show"),
    # path('delete/<int:id>', views.delete, name="documentos_delete"),
]