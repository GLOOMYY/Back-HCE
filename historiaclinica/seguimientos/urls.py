from django.urls import path
from .views import SeguimientoEspecialidadListView

# Importar Vistas

urlpatterns = [
    # SeguimientoEspecialidadRoutes
    path("especialidad/list/", SeguimientoEspecialidadListView.as_view()),
]
