from django.urls import path
from .views import HistoraClinicaListView

# Importar Vistas

# URLs de la HistoriaClinica

urlpatterns = [
    path(route="", view=HistoraClinicaListView.as_view()),
]
