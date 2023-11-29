from django.contrib import admin
from .models import (
    SeguimientoEspecialidad,
    SeguimientoMedicinaGeneral,
    SeguimientoEnfermeria,
    Estrategia,
    Formulario,
    SignosVitales,
    DatosAntropometricos,
    Observaciones,
    NotasAclaratorias,
)

# Register your models here.

admin.site.register(SeguimientoEnfermeria)
admin.site.register(SeguimientoMedicinaGeneral)
admin.site.register(SeguimientoEspecialidad)
admin.site.register(Estrategia)
admin.site.register(Formulario)
admin.site.register(SignosVitales)
admin.site.register(DatosAntropometricos)
admin.site.register(Observaciones)
admin.site.register(NotasAclaratorias)
