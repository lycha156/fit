from django.db import models
from socios.models import Socio

class Pago(models.Model):
    ESTADO_PAGO = [
        ('PAGO', 'Pago'),
        ('IMPAGO', 'Impago')
    ]

    socio = models.ForeignKey(Socio, verbose_name="Socio", on_delete=models.RESTRICT, related_name="socio_pago")
    mes = models.IntegerField("Mes")
    año = models.IntegerField("Año")
    estado = models.CharField("Estado", max_length=50, choices=ESTADO_PAGO)
    monto = models.FloatField("Monto")

