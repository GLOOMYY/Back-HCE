from rest_framework import serializers
from .models import HistoriaClinica

# Serializadores para HistoriaClinica


class HistoriaClinicaSerializer(serializers.ModelSerializer):
    """Serializador de la clase HistoriaClinica, incluye todos los campos"""

    class Meta:
        model = HistoriaClinica
        fields = "__all__"
