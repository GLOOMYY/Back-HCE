from django.contrib import admin
from .models import (
    Formularios,
    SignosVitales,
    DatosAntropometricos,
    Observaciones,
    NotasAclaratorias,
)

# Register your models here.

admin.site.register(Formularios)
admin.site.register(SignosVitales)
admin.site.register(DatosAntropometricos)
admin.site.register(Observaciones)
# admin.site.register(NotasAclaratorias)
