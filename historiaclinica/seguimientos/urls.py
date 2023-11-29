from django.urls import path
from .views import (
    SeguimientoEspecialidadListView,
    SeguimientoEspecialidadCreateView,
    SeguimientoMedicinaGeneralListView,
    SeguimientoMedicinaGeneralCreateView,
    SeguimientoEnfermeriaListView,
    SeguimientoEnfermeriaCreateView,
    EstrategiaListView,
    EstrategiaCreateView,
    FormularioListView,
    FormularioCreateView,
    SignosVitalesListView,
    SignosVitalesCreateView,
    DatosAntropometricosListView,
    DatosAntropometricosCreateView,
    ObservacionesListView,
    ObservacionesCreateView,
    NotasAclaratoriasListView,
    NotasAclaratoriasCreateView,
)

"""
    ListViews: Metodo GET
    CreateViews: Metodo POST
"""

urlpatterns = [
    # SeguimientoEspecialidadRoutes
    path(route="especialidad/", view=SeguimientoEspecialidadListView.as_view()),
    path(route="especialidad/create", view=SeguimientoEspecialidadCreateView.as_view()),
    # SeguimientoMedicinaGeneral
    path(route="general/", view=SeguimientoMedicinaGeneralListView.as_view()),
    path(route="general/create", view=SeguimientoMedicinaGeneralCreateView.as_view()),
    # SeguimientoEnfermeria
    path(route="enfermeria/", view=SeguimientoEnfermeriaListView.as_view()),
    path(route="enfermeria/create", view=SeguimientoEnfermeriaCreateView.as_view()),
    # Estrategia
    path(route="estrategia/", view=EstrategiaListView.as_view()),
    path(route="estrategia/create", view=EstrategiaCreateView.as_view()),
    # Formulario
    path(route="formulario/", view=FormularioListView.as_view()),
    path(route="formulario/create", view=FormularioCreateView.as_view()),
    # SignosVitales
    path(route="signos-vitales/", view=SignosVitalesListView.as_view()),
    path(route="signos-vitales/create", view=SignosVitalesCreateView.as_view()),
    # DatosAntropometricos
    path(route="datos-antropometricos/", view=DatosAntropometricosListView.as_view()),
    path(
        route="datos-antropometricos/create",
        view=DatosAntropometricosCreateView.as_view(),
    ),
    # Observaciones
    path(route="observaciones/", view=ObservacionesListView.as_view()),
    path(route="observaciones/create", view=ObservacionesCreateView.as_view()),
    # NotasAclaratorias
    path(route="notas-aclaratorias/", view=NotasAclaratoriasListView.as_view()),
    path(route="notas-aclaratorias/create", view=NotasAclaratoriasCreateView.as_view()),
]
