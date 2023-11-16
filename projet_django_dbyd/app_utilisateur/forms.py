from django import forms
from core.models import ActivitePhysique, Alimentation, AutreSymptome, EvaluationNiveauStress, InformationCardiaque, Physique, PriseMedicament

class ActivitePhysiqueForm(forms.ModelForm):
    class Meta:
        model = ActivitePhysique
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_activite_physique']

class AlimentationForm(forms.ModelForm):
    class Meta:
        model = Alimentation
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_alimentation']

class AutreSymptomForm(forms.ModelForm):
    class Meta:
        model = AutreSymptome
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_autre_symptome']
        widgets = {
            'debut_douleur_thoracique': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'HH:MM'}),
            'debut_palpitation': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'HH:MM'}),
            'debut_malaise': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'HH:MM'}),
        }
        labels = {
            'debut_douleur_thoracique': 'Heure de début de la douleur thoracique',
            'debut_palpitation': 'Heure de début des palpitations',
            'debut_malaise': 'Heure de début du malaise',
        }

class EvaluationNiveauStressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EvaluationNiveauStressForm, self).__init__(*args, **kwargs)
        self.fields['impact_stress'].widget.attrs['id'] = 'impact_stress'
        
    class Meta:
        model = EvaluationNiveauStress
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_evaluation_niveau_stress']

class InformationCardiaqueForm(forms.ModelForm):
    class Meta:
        model = InformationCardiaque
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_information_cardiaque']

class PhysiqueForm(forms.ModelForm):
    class Meta:
        model = Physique
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_physique']

class PriseMedicamentForm(forms.ModelForm):
    class Meta:
        model = PriseMedicament
        fields = '__all__'  # ou fields = ['champ1', 'champ2', ...]
        exclude = ['id_prise_medicament']