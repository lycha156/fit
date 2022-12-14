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

    # EJERCICIOS
    path('ejercicios/', views.ejercicios_index, name="ejercicios_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    # path('serie/create/', views.series_create, name="series_create"),
    path('ejercicios/create', views.ejercicios_create, name="ejercicios_create"),
    path('ejercicios/update/<int:id>', views.ejercicios_update, name="ejercicios_update"),
    # path('show/<int:id>/<int:agenda>', views.show, name="rutinas_show"),
    path('ejercicios/delete/<int:id>', views.ejercicios_delete, name="ejercicios_delete"),
    # path('generar_mes', views.generar_mes, name="agenda_generar_mes"),
]