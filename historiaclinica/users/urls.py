from django.urls import path
from .views import PacienteView, ProfesionalView

# Pendiente import de Views

urlpatterns = [
    # Profesional URLS
    path(route="profesional/list/", view=ProfesionalView.as_view()),
    # Paciente URLS
    path(route="paciente/list/", view=PacienteView.as_view()),
]
