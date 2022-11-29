from django.urls import path
from . import views

urlpatterns = [
    # PAGOS
    path('', views.index, name="pagos_index"),
    # path('create', views.create, name="socios_create"),
    # path('update/<int:id>', views.update, name="socios_update"),
    # path('show/<int:id>', views.show, name="socios_show"),
    # path('delete/<int:id>', views.delete, name="socios_delete"),
]