from rest_framework import serializers
from .models import SeguimientoEspecialidad


class SeguimientoEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoEspecialidad
        fields = "__all__"
