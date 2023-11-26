from rest_framework import generics
from .models import Profesional, Paciente
from .serializers import ProfesionalSerializer, PacienteSerializer

# Create your views here.


class ProfesionalView(generics.ListAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


class PacienteView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
