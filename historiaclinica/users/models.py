from django.db import models

# Create your models here.


class Profesional(models.Model):
    """Profesional de la salud"""

    TYPE_ESPECIALIDAD = [
        ("Enfermeria", "Enfermeria"),
        ("General", "General"),
        ("Oftamologia", "Oftamologia"),
    ]
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    especialidad = models.CharField(
        verbose_name="Especialidad", max_length=50, choices=TYPE_ESPECIALIDAD
    )

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"Nombre: {self.nombre} - Especialidad: {self.especialidad}"


class Paciente(models.Model):
    """Paciente"""

    documento = models.IntegerField(verbose_name="Cedula")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"Documento: {self.documento}"
