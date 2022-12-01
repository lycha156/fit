from django.db import models

class Socio(models.Model):
    ESTADO_SOCIO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo')
    ]

    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    fechanacimiento = models.DateField("Fecha de Nacimiento", blank=True, null=True, auto_now=False, auto_now_add=False)
    dni = models.IntegerField("DNI", blank=True, null=True)
    telefono = models.CharField("Telefono", max_length=50, blank=True)
    direccion = models.CharField("Direccion", max_length=50, blank=True)
    email = models.EmailField("Email", max_length=254, blank=True)
    estado = models.CharField("Estado", max_length=50, choices=ESTADO_SOCIO)
    observaciones = models.TextField("Observaciones")
    cuota = models.ForeignKey("socios.Cuota", on_delete=models.RESTRICT, related_name="cuota_socio")

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Cuota(models.Model):
    concepto = models.CharField("Concepto", max_length=50)
    monto = models.FloatField("Monto")

    def  __str__(self):
        return f"{self.concepto} - $ {self.monto}"
    
