from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
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
from .serializers import (
    SeguimientoEspecialidadSerializer,
    SeguimientoMedicinaGeneralSerializer,
    SeguimientoEnfermeriaSerializer,
    EstrategiaSerializer,
    FormularioSerializer,
    SignosVitalesSerializer,
    DatosAntropometricosSerializer,
    ObservacionesSerializer,
    NotasAclaratoriasSerializer,
)


# Vistas de SeguimientoEspecialidad


class SeguimientoEspecialidadListView(generics.ListAPIView):
    """
    Vista para listar SeguimientosEspecialidad
    Metodo GET
    """

    queryset = SeguimientoEspecialidad.objects.all()
    serializer_class = SeguimientoEspecialidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "historia"]


class SeguimientoEspecialidadCreateView(generics.CreateAPIView):
    """
    Vista para crear SeguimientosEspecialidad
    Metodo POST
    """

    queryset = SeguimientoEspecialidad.objects.all()
    serializer_class = SeguimientoEspecialidadSerializer


# Vistas de SeguimientoMedicinaGeneral
class SeguimientoMedicinaGeneralListView(generics.ListAPIView):
    """
    Vista para listar SeguimientosMedicinaGeneral
    Metodo GET
    """

    queryset = SeguimientoEspecialidad.objects.all()
    serializer_class = SeguimientoEspecialidadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "historia"]


class SeguimientoMedicinaGeneralCreateView(generics.CreateAPIView):
    """
    Vista para crear SeguimientosMedicinaGeneral
    Metodo POST
    """

    queryset = SeguimientoMedicinaGeneral.objects.all()
    serializer_class = SeguimientoMedicinaGeneralSerializer


# Vistas de SeguimientoEnfermeria
class SeguimientoEnfermeriaListView(generics.ListAPIView):
    """
    Vista para listar SeguimientosEnfermeria
    Metodo GET
    """

    queryset = SeguimientoEnfermeria.objects.all()
    serializer_class = SeguimientoEnfermeriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "historia"]


class SeguimientoEnfermeriaCreateView(generics.CreateAPIView):
    """
    Vista para crear SeguimientosEnfermeria
    Metodo POST
    """

    queryset = SeguimientoEnfermeria.objects.all()
    serializer_class = SeguimientoEnfermeriaSerializer


# Vistas de Estrategia
class EstrategiaListView(generics.ListAPIView):
    """
    Vista para listar Estrategias
    Metodo GET
    """

    queryset = Estrategia.objects.all()
    serializer_class = EstrategiaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "seguimiento_especialidad"]


class EstrategiaCreateView(generics.CreateAPIView):
    """
    Vista para crear Estrategias
    Metodo POST
    """

    queryset = Estrategia.objects.all()
    serializer_class = EstrategiaSerializer


# Vistas de Formulario
class FormularioListView(generics.ListAPIView):
    """
    Vista para listar Formularios
    Metodo GET
    """

    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer


class FormularioCreateView(generics.CreateAPIView):
    """
    Vista para crear Formularios
    Metodo POST
    """

    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer


# Vistas de SignosVitales
class SignosVitalesListView(generics.ListAPIView):
    """
    Vista para listar SignosVitales
    Metodo GET
    """

    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer


class SignosVitalesCreateView(generics.CreateAPIView):
    """
    Vista para crear SignosVitales
    Metodo POST
    """

    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer


# Vistas de DatosAntropometricos
class DatosAntropometricosListView(generics.ListAPIView):
    """
    Vista para listar DatosAntropometricos
    Metodo GET
    """

    queryset = DatosAntropometricos.objects.all()
    serializer_class = DatosAntropometricosSerializer


class DatosAntropometricosCreateView(generics.CreateAPIView):
    """
    Vista para crear DatosAntropometricos
    Metodo POST
    """

    queryset = DatosAntropometricos.objects.all()
    serializer_class = DatosAntropometricosSerializer


# Vistas de Observaciones
class ObservacionesListView(generics.ListAPIView):
    """
    Vista para listar Observaciones
    Metodo GET
    """

    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer


class ObservacionesCreateView(generics.CreateAPIView):
    """
    Vista para crear Observaciones
    Metodo POST
    """

    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer


# Vistas de NotasAclaratorias
class NotasAclaratoriasListView(generics.ListAPIView):
    """
    Vista para listar NotasAclaratorias
    Metodo GET
    """

    queryset = NotasAclaratorias.objects.all()
    serializer_class = NotasAclaratoriasSerializer


class NotasAclaratoriasCreateView(generics.CreateAPIView):
    """
    Vista para crear NotasAclaratorias
    Metodo POST
    """

    queryset = NotasAclaratorias.objects.all()
    serializer_class = NotasAclaratoriasSerializer
