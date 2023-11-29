from django.urls import path
from .views import (
    ProfesionalListView,
    ProfesionalCreateView,
    PacienteListView,
    PacienteCreateView,
)


urlpatterns = [
    # Profesional URLS
    path(route="profesional/", view=ProfesionalListView.as_view()),  # GET
    path(route="profesional/create", view=ProfesionalCreateView.as_view()),  # POST
    # Paciente URLS
    path(route="paciente/", view=PacienteListView.as_view()),  # GET
    path(route="paciente/create", view=PacienteCreateView.as_view()),  # POST
]
