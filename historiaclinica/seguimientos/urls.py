from django.urls import path
from .views import SeguimientoEspecialidadView

# Importar Vistas

urlpatterns = [
    path("seguimiento/list", SeguimientoEspecialidadView.as_view()),
]
