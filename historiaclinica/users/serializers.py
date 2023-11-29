from rest_framework import serializers
from .models import Paciente, Profesional


class ProfesionalSerializer(serializers.ModelSerializer):
    """Serializador del Profesional de la salud"""

    class Meta:
        model = Profesional
        fields = "__all__"


class PacienteSerializer(serializers.ModelSerializer):
    """Serializador del Paciente"""

    class Meta:
        model = Paciente
        fields = "__all__"
