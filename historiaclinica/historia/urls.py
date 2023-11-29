from django.urls import path
from .views import HistoraClinicaListView, HistoriaClinicaCreateView

# Importar Vistas

# URLs de la HistoriaClinica

urlpatterns = [
    path(route="", view=HistoraClinicaListView.as_view()),
    path(route="create/", view=HistoriaClinicaCreateView.as_view()),
]
