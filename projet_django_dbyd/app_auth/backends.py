from django.contrib.auth.backends import BaseBackend
from core.models import Patient, Medecin, Administrator

class backend_auth(BaseBackend):
    
    def authenticate(self, request, nom=None, prenom=None, password=None, **kwargs):
        try:
            patient = Patient.objects.get(nom_patient=nom, prenom_patient=prenom)
            if patient.password_patient == password:  # Notez que j'utilise une comparaison directe ici, ce qui n'est pas idéal en matière de sécurité. C'est une simplification pour l'exemple.
                # Ajoute une propriété pour indiquer le type d'utilisateur
                setattr(patient, 'user_type', 'patient')
                return patient
        except Patient.DoesNotExist:
            pass

        try:
            medecin = Medecin.objects.get(nom_medecin=nom, prenom_medecin=prenom)
            if medecin.password_medecin == password:  # Même remarque ici concernant la sécurité.
                # Ajoute une propriété pour indiquer le type d'utilisateur
                setattr(medecin, 'user_type', 'medecin')
                return medecin
        except Medecin.DoesNotExist:
            pass

        '''try:
            admin = Administrator.objects.get(nom_administrator=nom, prenom_administrator=prenom)
            if admin.password_administrator == password:  # Même remarque ici concernant la sécurité.
                # Ajoute une propriété pour indiquer le type d'utilisateur
                setattr(admin, 'user_type', 'administrator')
                return admin
        except Administrator.DoesNotExist:
            pass'''

        return None
