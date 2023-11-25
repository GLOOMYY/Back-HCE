from rest_framework import generics
from .models import SeguimientoEspecialidad
from .serializers import SeguimientoEspecialidadSerializer

# Create your views here.


class SeguimientoEspecialidadView(generics.ListAPIView):
    queryset = SeguimientoEspecialidad.objects.all()
    serializer_class = SeguimientoEspecialidadSerializer
