from django.contrib import admin
from .models import (
    Formulario,
    SignosVitales,
    DatosAntropometricos,
    Observaciones,
    NotasAclaratorias,
    SeguimientoEnfermeria,
    SeguimientoMedicinaGeneral,
    SeguimientoEspecialidad,
)

# Register your models here.

admin.site.register(SeguimientoEnfermeria)
admin.site.register(SeguimientoMedicinaGeneral)
admin.site.register(SeguimientoEspecialidad)
admin.site.register(Formulario)
admin.site.register(SignosVitales)
admin.site.register(DatosAntropometricos)
admin.site.register(Observaciones)
admin.site.register(NotasAclaratorias)
