from django.db import models
from users.models import Profesional, Paciente
from historia.models import HistoriaClinica

# Create your models here.
"""
class Ejemplo(models.Model o lo que necesites heredar):
    campo1 = models.CharField(verbose_name='Nombre del campo', max_length=50)
    campo2 = models.ForeingKey(Para Relacionar Modelos)
    
    class Meta:
        verbose_name = 'Ejemplo'
        verbose_name_plural = 'Ejemplos'
        
    def __str__(self):
        return f'Lo que se vaya a mostrar en el admin'
"""


class Seguimiento(models.Model):
    # Relacion
    historia = models.ForeignKey(to=HistoriaClinica, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Seguimiento"


class SeguimientoEspecialidad(Seguimiento):
    class Meta:
        verbose_name = "Seguimiento Especialidad"
        verbose_name_plural = "Seguimientos Especialidad"

    def __str__(self):
        return f"Seguimiento Especialidad:{self.id}"


class SeguimientoMedicinaGeneral(Seguimiento):
    class Meta:
        verbose_name = "Seguimiento Medicina General"
        verbose_name_plural = "Seguimientos Medicina General"

    def __str__(self):
        return f"Seguimiento Medicina General:{self.id}"


class SeguimientoEnfermeria(Seguimiento):
    class Meta:
        verbose_name = "Seguimiento Enfermeria"
        verbose_name_plural = "Seguimientos Enfermeria"

    def __str__(self):
        return f"Seguimiento Enfermeria:{self.id}"


class Estrategia(models.Model):
    # Relacion
    seguimiento_especialidad = models.ForeignKey(
        to=SeguimientoEspecialidad, on_delete=models.CASCADE
    )

    # Campos
    objetivo = models.TextField(verbose_name="Objetivo")
    subjetivo = models.TextField(verbose_name="Subjetivo")
    analisis = models.TextField(verbose_name="Analisis")
    plan = models.TextField(verbose_name="Plan")

    class Meta:
        verbose_name = "Estrategia"
        verbose_name_plural = "Estrategias"

    def __str__(self):
        return f"Estrategias:{self.id}"


class Formulario(models.Model):
    # Relaciones
    profesional = models.ForeignKey(to=Profesional, on_delete=models.CASCADE)
    paciente = models.ForeignKey(to=Paciente, on_delete=models.CASCADE)
    seguimiento_especialidad = models.ForeignKey(
        to=SeguimientoEspecialidad, on_delete=models.CASCADE
    )
    seguimiento_medicina_general = models.ForeignKey(
        to=SeguimientoMedicinaGeneral, on_delete=models.CASCADE
    )
    seguimiento_enfermeria = models.ForeignKey(
        to=SeguimientoEnfermeria, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    def __str__(self):
        return f"Formulario: {self.paciente}"


class SignosVitales(models.Model):
    # Relaciones
    formulario = models.ForeignKey(to=Formulario, on_delete=models.CASCADE)

    # Campos
    tension_arterial_sistolica = models.IntegerField(
        verbose_name="Tension Arterial Sistolica"
    )
    tension_diastolica = models.IntegerField(verbose_name="Tension Diastolica")
    frecuencia_respiratoria = models.IntegerField(
        verbose_name="Frecuencia Respiratoria"
    )
    saturacion_oxigeno = models.IntegerField(verbose_name="Saturacion Oxigeno")
    frecuencia_cardiaca = models.IntegerField(verbose_name="Frecuencia Cardiaca")

    class Meta:
        verbose_name = "Signos Vitales"
        verbose_name_plural = "Signos Vitales"

    def __str__(self):
        return f"Signos Vitales: {self.id}"


class DatosAntropometricos(models.Model):
    # Relaciones
    formulario = models.ForeignKey(to=Formulario, on_delete=models.CASCADE)

    # Campos
    talla = models.IntegerField(verbose_name="Talla")
    peso = models.IntegerField(verbose_name="Peso")
    observaciones = models.TextField(verbose_name="Observaciones Generales")

    class Meta:
        verbose_name = "Datos Antropometricos"
        verbose_name_plural = "Datos Antropometricos"

    def __str__(self):
        return f"Datos Antropometricos: {self.id}"


class Observaciones(models.Model):
    # Relaciones
    formulario = models.ForeignKey(to=Formulario, on_delete=models.CASCADE)

    # Campos
    observaciones = models.TextField(verbose_name="Observaciones")

    class Meta:
        verbose_name = "Observaciones"
        verbose_name_plural = "Observaciones"

    def __str__(self):
        return f"Observaciones:{self.id}"


class NotasAclaratorias(models.Model):
    # Relaciones
    formulario = models.ForeignKey(to=Formulario, on_delete=models.CASCADE)
    profesional = models.ForeignKey(to=Profesional, on_delete=models.CASCADE)
    historia = models.ForeignKey(to=HistoriaClinica, on_delete=models.CASCADE)

    # Campos
    contexto = models.TextField(verbose_name="Contexto")
    especialidad = models.CharField(verbose_name="Especialidad", max_length=50)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Nota Aclaratoria"
        verbose_name_plural = "Notas Aclaratorias"

    def __str__(self):
        return f"{self.fecha} Profesional:{self.profesional} Historia:{self.historia}"
