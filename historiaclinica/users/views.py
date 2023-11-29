from rest_framework import generics
from .models import Profesional, Paciente
from .serializers import ProfesionalSerializer, PacienteSerializer

# Create your views here.


# Vistas del Profesional de la salud


class ProfesionalView(generics.ListAPIView):
    """Vista que lista los Profesionales de la salud"""

    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


# Vistas del Paciente


class PacienteView(generics.ListAPIView):
    """Vista que lista los Pacientes"""

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
