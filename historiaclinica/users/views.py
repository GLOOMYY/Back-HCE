from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profesional, Paciente
from .serializers import ProfesionalSerializer, PacienteSerializer


# Vistas del Profesional de la salud


class ProfesionalListView(generics.ListAPIView):
    """
    Vista que lista los Profesionales de la salud
    Metodo GET
    """

    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["especialidad"]


class ProfesionalCreateView(generics.CreateAPIView):
    """
    Vista para crear Profesionales
    Metodo POST
    """

    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


# Vistas del Paciente


class PacienteListView(generics.ListAPIView):
    """
    Vista que lista los Pacientes
    Metodo GET
    """

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class PacienteCreateView(generics.CreateAPIView):
    """
    Vista para crear Pacientes
    Metodo POST
    """

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
