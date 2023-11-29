from rest_framework import generics
from .models import SeguimientoEspecialidad, SeguimientoMedicinaGeneral
from .serializers import (
    SeguimientoEspecialidadSerializer,
    SeguimientoMedicinaGeneralSerializer,
)

# Create your views here.


# Vistas de SeguimientoEspecialidad


class SeguimientoEspecialidadListView(generics.ListAPIView):
    queryset = SeguimientoEspecialidad.objects.all()
    serializer_class = SeguimientoEspecialidadSerializer


# Vistas de SeguimientoMedicinaGeneral


class SeguimientoMedicinaGeneralListView(generics.ListAPIView):
    queryset = SeguimientoMedicinaGeneral.objects.all()
    serializer_class = SeguimientoMedicinaGeneralSerializer
