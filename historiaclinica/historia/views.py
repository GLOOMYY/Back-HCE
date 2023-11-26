from rest_framework import generics
from .models import HistoriaClinica
from .serializers import HistoriaClinicaSerializer

# Create your views here.


class HistoraClinicaView(generics.ListAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
