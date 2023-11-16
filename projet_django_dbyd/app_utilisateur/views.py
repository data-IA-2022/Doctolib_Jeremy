from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.utils import timezone
from django.http import  HttpResponse
from django.db import transaction
from core.custom_decorators import custom_login_required_patient
from .forms import *
from core.models import *













# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page d'atterissage quand le patient doit remplir un formulaire

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def patient(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

    print ("---------------------------------------------- RAPPORT PAGE PATIENT ----------------------------------------------")
    if 'nom_patient' in request.session and 'prenom_patient' in request.session:
        print("Session existante dans la page administration :")
        print("Nom du patient :", request.session['nom_patient'])
        print("Prénom du patient :", request.session['prenom_patient'])
    else:
        print("Aucune session active.")
    print ("------------------------------------------------------------------------------------------------------------------")

        
    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte
    }
    return render(request, 'patient.html', context)













# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page de formulaire

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def formulaire(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

    date_post = timezone.now()

    if request.method == 'POST':

        form_activite_physique = ActivitePhysiqueForm(request.POST)
        form_alimentation = AlimentationForm(request.POST)
        form_autre_symptome = AutreSymptomForm(request.POST)
        form_evaluation_niveau_stress = EvaluationNiveauStressForm(request.POST)
        form_information_cardiaque = InformationCardiaqueForm(request.POST)
        form_physique = PhysiqueForm(request.POST)
        form_prise_medicament = PriseMedicamentForm(request.POST)

        if (form_activite_physique.is_valid() and form_alimentation.is_valid() and form_autre_symptome.is_valid() and
            form_evaluation_niveau_stress.is_valid() and form_information_cardiaque.is_valid() and form_physique.is_valid() and
            form_prise_medicament.is_valid()):
            # Aide a l'intégrité des données
            with transaction.atomic():

                # Récupérez l'instance de Patient en utilisant l'ID stocké dans la session
                patient_id = request.session.get('id_patient')

                try:
                    patient = Patient.objects.get(id_patient=patient_id)  # Assurez-vous que Patient est votre modèle d'utilisateur
                except Patient.DoesNotExist:
                    # Gérez l'erreur si l'ID de patient n'existe pas
                    return HttpResponse("Patient non trouvé", status=404)

                if patient:

                    # Créez une instance de Reponse et enregistrez-la pour obtenir l'id_reponse
                    reponse = Reponse(date_reponse=date_post, fk_utilisateur=patient)
                    reponse.save()

                    # Maintenant, créez et sauvegardez chaque instance du modèle lié avec la référence à l'instance de Reponse
                    activite_physique = form_activite_physique.save(commit=False)
                    activite_physique.reponse = reponse  # Supposons que votre modèle ActivitePhysique ait un champ reponse comme ForeignKey
                    activite_physique.save()

                    alimentation = form_alimentation.save(commit=False)
                    alimentation.reponse = reponse  # De même pour Alimentation
                    alimentation.save()

                    autre_symptome = form_autre_symptome.save(commit=False)
                    autre_symptome.reponse = reponse
                    autre_symptome.save()

                    evaluation_niveau_stress = form_evaluation_niveau_stress.save(commit=False)
                    evaluation_niveau_stress.reponse = reponse
                    evaluation_niveau_stress.save()

                    information_cardiaque = form_information_cardiaque.save(commit=False)
                    information_cardiaque.reponse = reponse
                    information_cardiaque.save()

                    physique = form_physique.save(commit=False)
                    physique.reponse = reponse
                    physique.save()

                    prise_medicament = form_prise_medicament.save(commit=False)
                    prise_medicament.reponse = reponse
                    prise_medicament.save()

                    # Après avoir enregistré tous les modèles liés remapper les id
                    reponse.fk_activite_physique = activite_physique
                    reponse.fk_alimentation = alimentation
                    reponse.fk_autre_symptome = autre_symptome
                    reponse.fk_evaluation_niveau_stress = evaluation_niveau_stress
                    reponse.fk_information_cardiaque = information_cardiaque
                    reponse.fk_physique = physique
                    reponse.fk_prise_medicament = prise_medicament
                    reponse.save()

                    return redirect('reponse_sauvegarder')
                else:
                    # Gérez le cas où l'instance du patient n'est pas trouvée
                    pass
        
    else:
        form_activite_physique = ActivitePhysiqueForm()
        form_alimentation = AlimentationForm()
        form_autre_symptome = AutreSymptomForm()
        form_evaluation_niveau_stress = EvaluationNiveauStressForm()
        form_information_cardiaque = InformationCardiaqueForm()
        form_physique = PhysiqueForm()
        form_prise_medicament = PriseMedicamentForm()

    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte,
        'date_post':date_post,
        'form_activite_physique': form_activite_physique,
        'form_alimentation': form_alimentation,
        'form_autre_symptome': form_autre_symptome,
        'form_evaluation_niveau_stress': form_evaluation_niveau_stress,
        'form_information_cardiaque': form_information_cardiaque,
        'form_physique': form_physique,
        'form_prise_medicament': form_prise_medicament,
    }
    return render(request, 'formulaire.html', context)














# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page d'atterissage quand le patient a déjà rempli un formulaire ce mois-ci

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def formulaire_deja_rempli(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

    print ("---------------------------------------------- RAPPORT FORMULAIRE DEJA REMPLI ----------------------------------------------")
    if 'nom_patient' in request.session and 'prenom_patient' in request.session:
        print("Session existante dans la page administration :")
        print("Nom du patient :", request.session['nom_patient'])
        print("Prénom du patient :", request.session['prenom_patient'])
    else:
        print("Aucune session active.")
    print ("----------------------------------------------------------------------------------------------------------------------------")

    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte
    }

    return render(request, 'formulaire_deja_rempli.html', context)











# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page de correction du formulaire

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def formulaire_correction(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

    patient = Patient.objects.get(id_patient=id_patient_connecte)

    # Récupérer la dernière réponse du patient.
    derniere_reponse = Reponse.objects.filter(fk_utilisateur=patient).order_by('-date_reponse').first()

    # Convertir l'objet réponse en dictionnaire pour avoir la valeure des fk
    reponse_dict = model_to_dict(derniere_reponse)
    print(reponse_dict)
 
    # Récupération de l'instance de l'objet à mettre à jour...
    objet_activite_physique = ActivitePhysique.objects.get(id_activite_physique=reponse_dict['fk_activite_physique'])
    objet_alimentation = Alimentation.objects.get(id_alimentation=reponse_dict['fk_alimentation'])
    objet_autre_symptome = AutreSymptome.objects.get(id_autre_symptome=reponse_dict['fk_autre_symptome'])
    objet_evaluation_niveau_stress = EvaluationNiveauStress.objects.get(id_evaluation_niveau_stress=reponse_dict['fk_evaluation_niveau_stress'])
    objet_information_cardiaque = InformationCardiaque.objects.get(id_information_cardiaque=reponse_dict['fk_information_cardiaque'])
    objet_physique = Physique.objects.get(id_physique=reponse_dict['fk_physique'])
    objet_prise_medicament = PriseMedicament.objects.get(id_prise_medicament=reponse_dict['fk_prise_medicament'])

    if request.method == 'POST':

        form_activite_physique = ActivitePhysiqueForm(request.POST, instance=objet_activite_physique)
        form_alimentation = AlimentationForm(request.POST, instance=objet_alimentation)
        form_autre_symptome = AutreSymptomForm(request.POST, instance=objet_autre_symptome)
        form_evaluation_niveau_stress = EvaluationNiveauStressForm(request.POST, instance=objet_evaluation_niveau_stress)
        form_information_cardiaque = InformationCardiaqueForm(request.POST, instance=objet_information_cardiaque)
        form_physique = PhysiqueForm(request.POST, instance=objet_physique)
        form_prise_medicament = PriseMedicamentForm(request.POST, instance=objet_prise_medicament)
        
        if (form_activite_physique.is_valid() and form_alimentation.is_valid() and form_autre_symptome.is_valid() and
            form_evaluation_niveau_stress.is_valid() and form_information_cardiaque.is_valid() and form_physique.is_valid() and
            form_prise_medicament.is_valid()):

            form_activite_physique.save()
            form_alimentation.save()
            form_autre_symptome.save()
            form_evaluation_niveau_stress.save()
            form_information_cardiaque.save()
            form_physique.save()
            form_prise_medicament.save()

            return redirect('correction_reussie')

    else:
        form_activite_physique = ActivitePhysiqueForm(instance=objet_activite_physique)
        form_alimentation = AlimentationForm(instance=objet_alimentation)
        form_autre_symptome = AutreSymptomForm(instance=objet_autre_symptome)
        form_evaluation_niveau_stress = EvaluationNiveauStressForm(instance=objet_evaluation_niveau_stress)
        form_information_cardiaque = InformationCardiaqueForm(instance=objet_information_cardiaque)
        form_physique = PhysiqueForm(instance=objet_physique)
        form_prise_medicament = PriseMedicamentForm(instance=objet_prise_medicament)


    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte,
        'derniere_reponse':reponse_dict,
        'form_activite_physique': form_activite_physique,
        'form_alimentation': form_alimentation,
        'form_autre_symptome': form_autre_symptome,
        'form_evaluation_niveau_stress': form_evaluation_niveau_stress,
        'form_information_cardiaque': form_information_cardiaque,
        'form_physique': form_physique,
        'form_prise_medicament': form_prise_medicament,
    }
    return render(request, 'formulaire_correction.html', context)














# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page quand un formulaire a été corrigé

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def correction_reussie(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

        
    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte
    }
    return render(request, 'correction_reussie.html', context)
















# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Page quand un formulaire a été sauvegarder

@custom_login_required_patient # décorateur custom pour bloquer l'accés sans séssion
def reponse_sauvegarder(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom = request.session.get('nom_patient', '')
    prenom = request.session.get('prenom_patient', '')
    id_patient_connecte = request.session.get('id_patient', '')
    # --------------------------------------------

        
    context = {
        'nom':nom,
        'prenom':prenom,
        'id_patient':id_patient_connecte
    }
    return render(request, 'reponse_sauvegarder.html', context)
