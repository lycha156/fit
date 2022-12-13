from django.urls import path
from rutinas import views

urlpatterns = [
    # RUTINAS
    path('', views.index, name="rutinas_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    # path('create/turno', views.create_turno, name="agenda_create_turno"),
    # path('create/evento', views.create_evento, name="agenda_create_evento"),
    # path('update/<str:evento>/<int:id>', views.update, name="agenda_update"),
    path('show/<int:id>/<int:agenda>', views.show, name="rutinas_show"),
    # path('delete/<int:id>', views.delete, name="agenda_delete"),
    # path('generar_mes', views.generar_mes, name="agenda_generar_mes"),

    # SERIES
    # path('', views.index, name="rutinas_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    path('serie/create/', views.series_create, name="series_create"),
    # path('create/evento', views.create_evento, name="agenda_create_evento"),
    # path('update/<str:evento>/<int:id>', views.update, name="agenda_update"),
    # path('show/<int:id>/<int:agenda>', views.show, name="rutinas_show"),
    # path('delete/<int:id>', views.delete, name="agenda_delete"),
    # path('generar_mes', views.generar_mes, name="agenda_generar_mes"),
]