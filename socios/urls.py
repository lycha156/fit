from django.urls import path
from . import views

urlpatterns = [
    # SOCIOS
    path('', views.index, name="socios_index"),
    path('create', views.create, name="socios_create"),
    path('update/<int:id>', views.update, name="socios_update"),
    path('show/<int:id>', views.show, name="socios_show"),
    path('delete/<int:id>', views.delete, name="socios_delete"),

    # CUOTAS
    path('cuotas', views.cuotas_index, name="cuotas_index"),
    path('cuotas/create', views.cuotas_create, name="cuotas_create"),
    path('cuotas/update/<int:id>', views.cuotas_update, name="cuotas_update"),
    # path('show/<int:id>', views.show, name="dependencias_show"),
    path('cuotas/delete/<int:id>', views.cuotas_delete, name="cuotas_delete"),
]