from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import HistoriaClinica
from .serializers import HistoriaClinicaSerializer


# Create your views here.


# Vistas de la HistoriaClinica


class HistoraClinicaListView(generics.ListAPIView):
    """Vista para listar todas las HistoriasClinicas"""

    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["paciente"]
