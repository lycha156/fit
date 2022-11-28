from django.db import models
from pagos.models import Cuota

class Socio(models.Model):
    ESTADO_SOCIO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo')
    ]

    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    fechanacimiento = models.DateField("Fecha de Nacimiento", auto_now=False, auto_now_add=False)
    dni = models.IntegerField("DNI")
    telefono = models.CharField("Telefono", max_length=50)
    direccion = models.CharField("Direccion", max_length=50)
    email = models.EmailField("Email", max_length=254)
    estado = models.CharField("Estado", max_length=50, choices=ESTADO_SOCIO)
    obsevaciones = models.TextField("Observaciones")
    cuota = models.ForeignKey(Cuota, verbose_name="Cuota", on_delete=models.RESTRICT, related_name="cuota_socio")

