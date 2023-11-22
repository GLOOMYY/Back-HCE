from django.db import models

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


class SignosVitales(models.Model):
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
        return f"Signos Vitales"


class DatosAntropometricos(models.Model):
    talla = models.IntegerField(verbose_name="Talla")
    peso = models.IntegerField(verbose_name="Peso")
    observaciones = models.TextField(verbose_name="Observaciones Generales")

    class Meta:
        verbose_name = "Datos Antropometricos"
        verbose_name_plural = "Datos Antropometricos"

    def __str__(self):
        return f"Datos Antropometricos"


class Observaciones(models.Model):
    observaciones = models.TextField(verbose_name="Observaciones")

    class Meta:
        verbose_name = "Observaciones"
        verbose_name_plural = "Observaciones"

    def __str__(self):
        return f"Observaciones"


# Leer mañada de ManyToManyField
class NotasAclaratorias:
    contexto = models.TextField(verbose_name="Contexto")
    especialidad = models.CharField(verbose_name="Especialidad", max_length=50)
    fecha = models.DateField(auto_now_add=True)
    # Profesional = Debe ser ForeingKey
