from django.urls import path
from . import views

urlpatterns = [
    path('medecin', views.medecin, name='medecin'),
    path('medecin/compte_medecin', views.compte_medecin, name='compte_medecin'),
    path('medecin/compte_medecin/correction_compte_medecin', views.correction_compte_medecin, name='correction_compte_medecin'),
    path('medecin/fiche_patient', views.fiche_patient, name='fiche_patient'),
    path('medecin/fiche_patient/correction_compte_patient', views.correction_compte_patient, name='correction_compte_patient'),
    path('medecin/ajout_patient', views.ajout_patient, name='ajout_patient'),
    path('medecin/resultat_etude', views.resultat_etude, name='resultat_etude'),
    path('medecin/compte_medecin/correction_compte_medecin/validation_correction_compte_medecin', views.validation_correction_compte_medecin, name='validation_correction_compte_medecin'),
     path('medecin/ajout_patient/validation_ajout_patient', views.validation_ajout_patient, name='validation_ajout_patient'),
]