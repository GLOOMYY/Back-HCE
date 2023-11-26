from django.urls import path
from .views import HistoraClinicaView

# Importar Vistas

urlpatterns = [
    path(route="list/", view=HistoraClinicaView.as_view()),
]
