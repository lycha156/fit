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
    
class Horario(models.Model):

    socio = models.ForeignKey('socios.Socio', verbose_name="Socio", on_delete=models.CASCADE, related_name="socio_horario", unique=True)
    lunes = models.BooleanField("Lunes", blank=True, null=True, default=False)
    lunesHorario = models.TimeField("Horario Lunes", auto_now=False, auto_now_add=False, blank=True, null=True)
    martes = models.BooleanField("Martes", blank=True, null=True, default=False)
    martesHorario = models.TimeField("Horario Martes", auto_now=False, auto_now_add=False, blank=True, null=True)
    miercoles = models.BooleanField("Miercoles", blank=True, null=True, default=False)
    miercolesHorario = models.TimeField("Horario Miercoles", auto_now=False, auto_now_add=False, blank=True, null=True)
    jueves = models.BooleanField("Jueves", blank=True, null=True, default=False)
    juevesHorario = models.TimeField("Horario Jueves", auto_now=False, auto_now_add=False, blank=True, null=True)
    viernes = models.BooleanField("Viernes", blank=True, null=True, default=False)
    viernesHorario = models.TimeField("Horario Viernes", auto_now=False, auto_now_add=False, blank=True, null=True)
    sabado = models.BooleanField("Sabado", blank=True, null=True, default=False)
    sabadoHorario = models.TimeField("Horario Sabado", auto_now=False, auto_now_add=False, blank=True, null=True)
    domingo = models.BooleanField("Domingo", blank=True, null=True, default=False)
    domingoHorario = models.TimeField("Horario Domingo", auto_now=False, auto_now_add=False, blank=True, null=True)
    
    def horario_id(self):
        return f'{self.id}'

    def __str__(self):
        salida = ""
        if self.lunes == True:
            salida += str('LUN (' + self.lunesHorario.strftime("%H:%M") + '), ')
        if self.martes == True:
            salida += str('MAR (' + self.martesHorario.strftime("%H:%M") + '), ')
        if self.miercoles == True:
            salida += str('MIE (' + self.miercolesHorario.strftime("%H:%M") + '), ')
        if self.jueves == True:
            salida += str('JUE (' + self.juevesHorario.strftime("%H:%M") + '), ')
        if self.viernes == True:
            salida += str('VIE (' + self.viernesHorario.strftime("%H:%M") + '), ')
        if self.sabado == True:
            salida += str('SAB (' + self.sabadoHorario.strftime("%H:%M") + '), ')
        if self.domingo == True:
            salida += str('DOM (' + self.domingoHorario.strftime("%H:%M") + '), ')
        if salida == "":
            salida = f'{self.socio} No tiene horario definido.-'
        return salida