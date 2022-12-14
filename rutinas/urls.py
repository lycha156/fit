from django.urls import path
from rutinas import views

urlpatterns = [
    # RUTINAS
    path('', views.index, name="rutinas_index"),
    # path('socio/<int:id>', views.pagos_socio, name="pagos_socio"),
    # path('create/turno', views., name="rutinas_create"),
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
    path('serie/delete/<int:id>', views.series_delete, name="series_delete"),
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

    # ELEMENTOS
    path('elementos/create/<int:contenedor_id>', views.elementos_create, name="elementos_create"),
    path('elementos/update/<int:id>', views.elementos_update, name="elementos_update"),
    path('elementos/elementos_delete/<int:id>', views.elementos_delete, name="elementos_delete"),
    path('elementos/ejercicios_ajax/', views.ejercicios_ajax, name="ejercicios_ajax"),

    # MODELOS RUTINAS
    path('modelos/', views.modelos_index, name="modelos_rutinas_index"),
    path('modelos/create/', views.modelos_create, name="modelos_rutinas_create"),
    path('modelos/update/<int:id>', views.modelos_update, name="modelos_rutinas_update"),
    path('modelos/delete/<int:id>', views.modelos_delete, name="modelos_rutinas_delete"),
    path('modelos/show/<int:id>', views.modelos_show, name="modelos_rutinas_show"),
    # path('elementos/ejercicios_ajax/', views.ejercicios_ajax, name="ejercicios_ajax"),

    # MODELOS SERIES
    path('modelos/series/create', views.modelos_series_create, name="modelos_series_create"),
    # path('modelos/series/update/<int:id>', views.modelos_series_update, name="modelos_series_update"),
    path('modelos/series/delete/<int:id>', views.modelos_series_delete, name="modelos_series_delete"),

    # MODELOS ELEMENTOS
    path('modelos/elementos/create/<int:contenedor_id>', views.modelos_elementos_create, name="C"),

]