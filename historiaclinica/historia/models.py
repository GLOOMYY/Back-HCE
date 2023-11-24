from django.db import models
from users.models import Profesional, Paciente

# Create your models here.


class HistoriaClinica(models.Model):
    """Agrupa toda la historia clinica de un paciente"""

    # Relaciones
    paciente = models.ForeignKey(to=Paciente, on_delete=models.CASCADE)

    # Campos
    contexto = models.TextField(verbose_name="Contexto")
    fecha = models.DateField(verbose_name="Fecha", auto_now_add=True)
    hora = models.TimeField(verbose_name="Hora", auto_now=True)
    codigo = models.IntegerField(verbose_name="Codigo")

    class Meta:
        verbose_name = "Historia Clinica"
        verbose_name_plural = "Historias Clinicas"

    def __str__(self) -> str:
        return f"Historia clinica de {self.paciente}"
