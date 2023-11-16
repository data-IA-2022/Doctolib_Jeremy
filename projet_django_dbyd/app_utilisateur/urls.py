from django.urls import path
from . import views

urlpatterns = [
    path('patient', views.patient, name='patient'),
    path('formulaire_deja_rempli', views.formulaire_deja_rempli, name='formulaire_deja_rempli'),
    path('formulaire_deja_rempli/formulaire_correction', views.formulaire_correction, name='formulaire_correction'),
    path('patient/formulaire', views.formulaire, name='formulaire'),
    path('formulaire_deja_rempli/formulaire_correction/correction_reussie', views.correction_reussie, name='correction_reussie'),
    path('patient/formulaire/reponse_sauvegarder', views.reponse_sauvegarder, name='reponse_sauvegarder'),
]