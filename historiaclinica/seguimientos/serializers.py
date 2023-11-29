from rest_framework import serializers
from .models import (
    SeguimientoEspecialidad,
    SeguimientoMedicinaGeneral,
    SeguimientoEnfermeria,
    Estrategia,
    Formulario,
    SignosVitales,
    DatosAntropometricos,
    Observaciones,
    NotasAclaratorias,
)


class SeguimientoEspecialidadSerializer(serializers.ModelSerializer):
    """Serializador del SeguimientoEspecialidad"""

    class Meta:
        model = SeguimientoEspecialidad
        fields = "__all__"


class SeguimientoMedicinaGeneralSerializer(serializers.ModelSerializer):
    """Serializador del SeguimientoMedicinaGeneral"""

    class Meta:
        model = SeguimientoMedicinaGeneral
        fields = "__all__"


class SeguimientoEnfermeriaSerializer(serializers.ModelSerializer):
    """Serializador del SeguimientoEnfermeria"""

    class Meta:
        model = SeguimientoEnfermeria
        fields = "__all__"


class EstrategiaSerializer(serializers.ModelSerializer):
    """Serializador de Estrategia"""

    class Meta:
        model = Estrategia
        fields = "__all__"


class FormularioSerializer(serializers.ModelSerializer):
    """Serializador de Formulario"""

    class Meta:
        model = Formulario
        fields = "__all__"


class SignosVitalesSerializer(serializers.ModelSerializer):
    """Serializador de SignosVitales"""

    class Meta:
        model = SignosVitales
        fields = "__all__"


class DatosAntropometricosSerializer(serializers.ModelSerializer):
    """Serializador de DatosAntropometricos"""

    class Meta:
        model = DatosAntropometricos
        fields = "__all__"


class ObservacionesSerializer(serializers.ModelSerializer):
    """Serializador de Observaciones"""

    class Meta:
        model = Observaciones
        fields = "__all__"


class NotasAclaratoriasSerializer(serializers.ModelSerializer):
    """Serializador de NotasAclaratorias"""

    class Meta:
        model = NotasAclaratorias
        fields = "__all__"
