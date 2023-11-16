from django import forms
from core.models import Medecin, Patient

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_medecin', 'nom_medecin', 'prenom_medecin', 'fk_nom_administrator', 'fk_id_administrator']
        labels = {
            'mail_medecin': 'Votre Email :',
            'password_medecin': 'Password :',
            'tel_medecin': 'Votre numéro de téléphone : +33',
            'specialite_medecin': 'Spécialité :',
            'last_login': 'Date de la dernière connexion :',
            # autres champs et leurs labels personnalisés
        }

class PatientForm(forms.ModelForm):
    fk_id_medecin = forms.ModelChoiceField(queryset=Medecin.objects.all(), widget=forms.HiddenInput())
    fk_nom_medecin = forms.ModelChoiceField(queryset=Medecin.objects.all(), widget=forms.HiddenInput())
    password_patient = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Patient
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_patient', 'last_login']