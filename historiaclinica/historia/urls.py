from django.urls import path
from .views import HistoraClinicaListView, HistoriaClinicaCreateView


# URLs de la HistoriaClinica

urlpatterns = [
    path(route="", view=HistoraClinicaListView.as_view()),  # GET
    path(route="create/", view=HistoriaClinicaCreateView.as_view()),  # POST
]
