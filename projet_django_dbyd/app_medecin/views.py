from django.shortcuts import render, redirect
from core.custom_decorators import custom_login_required_medecin
from django.forms.models import model_to_dict
from app_medecin.generer_mdp import generate_random_password
from app_medecin.send_mail_mailgun import send_mail_with_mailgun
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from core.models import *


# -------------------------------------------------------------------------------------------- Landing page accueil medecin
@custom_login_required_medecin
def medecin(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin = request.session.get('id_medecin', '')
    # --------------------------------------------

    print ("---------------------------------------------- RAPPORT PAGE MEDECIN ----------------------------------------------")
    if 'nom_medecin' in request.session and 'prenom_medecin' in request.session:
        print("Session existante dans la page medecin :")
        print("Nom du medecin :", request.session['nom_medecin'])
        print("Prénom du medecin :", request.session['prenom_medecin'])
    else:
        print("Aucune session active.")
    print ("------------------------------------------------------------------------------------------------------------------")

    return render(request, 'accueil_medecin.html', {'nom_medecin': nom_medecin, 'prenom_medecin': prenom_medecin, 'id_medecin':id_medecin})











# -------------------------------------------------------------------------------------------- Page compte medecin
@custom_login_required_medecin
def compte_medecin(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

    donnee_medecin = Medecin.objects.get(id_medecin=id_medecin_connecte)

    reponse_dict = model_to_dict(donnee_medecin)
    print(reponse_dict)

    context = {
        'nom_medecin': nom_medecin, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin_connecte':id_medecin_connecte,
        'reponse_dict':reponse_dict
    }

    return render(request, 'compte_medecin.html', context)











# -------------------------------------------------------------------------------------------- Page correction compte medecin
@custom_login_required_medecin
def correction_compte_medecin(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

    donnee_medecin = Medecin.objects.get(id_medecin=id_medecin_connecte)

    reponse_dict = model_to_dict(donnee_medecin)
    print(reponse_dict)

    if request.method == 'POST':

        form_medecin = MedecinForm(request.POST, instance=donnee_medecin)
        
        if form_medecin.is_valid():

            form_medecin.save()

            return redirect('validation_correction_compte_medecin')

    else:
        form_medecin = MedecinForm(instance=donnee_medecin)

    context = {
        'nom_medecin': nom_medecin, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin_connecte':id_medecin_connecte,
        'form_medecin':form_medecin,
    }

    return render(request, 'correction_compte_medecin.html', context)




# -------------------------------------------------------------------------------------------- Page correction fiche patient
@custom_login_required_medecin
def fiche_patient(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

    donnee_medecin = Medecin.objects.get(id_medecin=id_medecin_connecte)
    medecin = model_to_dict(donnee_medecin)
    print(medecin)

    mes_patients = Patient.objects.filter(fk_id_medecin=medecin['id_medecin'])
    liste_des_patients = [model_to_dict(patient) for patient in mes_patients]

    liste_des_infos = []

    for patient in mes_patients:
        reponses = Reponse.objects.filter(fk_utilisateur=patient.id_patient)
        for reponse in reponses:
            infos = {
                'id_patient': patient.id_patient,
                'id_reponse': reponse.id_reponse,
                'date_reponse': reponse.date_reponse,
            }

            if reponse.fk_physique_id:
                physique = Physique.objects.get(id_physique=reponse.fk_physique_id)
                infos['poids'] = physique.poids
                infos['tour_de_taille_cm'] = physique.tour_de_taille_cm
            
            if reponse.fk_information_cardiaque_id:
                informationcardiaque = InformationCardiaque.objects.get(id_information_cardiaque=reponse.fk_information_cardiaque_id)
                infos['frequence_cardiaque_par_min'] = informationcardiaque.frequence_cardiaque_par_min
                infos['ta_systolique_matin'] = informationcardiaque.ta_systolique_matin
                infos['ta_systolique_soir'] = informationcardiaque.ta_systolique_soir
                infos['ta_diastolique_matin'] = informationcardiaque.ta_diastolique_matin
                infos['ta_diastolique_soir'] = informationcardiaque.ta_diastolique_soir
                infos['symptome_cardiovasculaire'] = informationcardiaque.symptome_cardiovasculaire

            if reponse.fk_alimentation_id:
                alimentation = Alimentation.objects.get(id_alimentation=reponse.fk_alimentation_id)
                infos['consommation_alcool'] = alimentation.consommation_alcool
                infos['grignotage_sale'] = alimentation.grignotage_sale
                infos['grignotage_sucre'] = alimentation.grignotage_sucre
                infos['nb_repas_journee_en_cours'] = alimentation.nb_repas_journee_en_cours
                infos['quantite_eau_bu'] = alimentation.quantite_eau_bu
                infos['quantite_alcool_bu'] = alimentation.quantite_alcool_bu

            if reponse.fk_activite_physique_id:
                activitephysique = ActivitePhysique.objects.get(id_activite_physique=reponse.fk_activite_physique_id)
                infos['activite_physique_journee_en_cours'] = activitephysique.activite_physique_journee_en_cours
                infos['nature_activite_physique'] = activitephysique.nature_activite_physique
                infos['duree_activite_physique_en_min'] = activitephysique.duree_activite_physique_en_min

            if reponse.fk_prise_medicament_id:
                prisemedicament = PriseMedicament.objects.get(id_prise_medicament=reponse.fk_prise_medicament_id)
                infos['nb_medicament_pris_dans_la_journee'] = prisemedicament.nb_medicament_pris_dans_la_journee
                infos['oublie_medic_matin'] = prisemedicament.oublie_medic_matin
                infos['oublie_medic_soir'] = prisemedicament.oublie_medic_soir
                infos['effet_secondaire'] = prisemedicament.effet_secondaire
                infos['symptome_particulier'] = prisemedicament.symptome_particulier
                infos['effet_secondaire_ou_symptome_description'] = prisemedicament.effet_secondaire_ou_symptome_description

            if reponse.fk_autre_symptome_id:
                autresymptome = AutreSymptome.objects.get(id_autre_symptome=reponse.fk_autre_symptome_id)
                infos['dyspnee'] = autresymptome.dyspnee
                infos['oedeme'] = autresymptome.oedeme
                infos['episode_infectieux'] = autresymptome.episode_infectieux
                infos['fievre'] = autresymptome.fievre
                infos['palpitation'] = autresymptome.palpitation
                infos['debut_palpitation'] = autresymptome.debut_palpitation
                infos['duree_palpitation_en_min'] = autresymptome.duree_palpitation_en_min
                infos['douleur_thoracique'] = autresymptome.douleur_thoracique
                infos['debut_douleur_thoracique'] = autresymptome.debut_douleur_thoracique
                infos['duree_douleur_thoracique_en_min'] = autresymptome.duree_douleur_thoracique_en_min
                infos['malaise'] = autresymptome.malaise
                infos['debut_malaise'] = autresymptome.debut_malaise
                infos['duree_malaise_en_min'] = autresymptome.duree_malaise_en_min

            liste_des_infos.append(infos)

    for info in liste_des_infos:
        print(info)

    context = {
        'nom_medecin': nom_medecin, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin_connecte':id_medecin_connecte,
        'patients': liste_des_patients,
        'liste_des_infos':liste_des_infos,
    }

    return render(request, 'fiche_patient.html', context)







# -------------------------------------------------------------------------------------------- Page correction compte patient
@custom_login_required_medecin
def correction_compte_patient(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

    donnee_medecin = Medecin.objects.get(id_medecin=id_medecin_connecte)
    medecin = model_to_dict(donnee_medecin)
    print(medecin)

    context = {
        'nom_medecin': nom_medecin, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin_connecte':id_medecin_connecte
    }

    return render(request, 'correction_compte_patient.html', context)






# -------------------------------------------------------------------------------------------- Page ajout patient
@custom_login_required_medecin
def ajout_patient(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin_connecte = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

    if request.method == 'POST':
        form_patient = PatientForm(request.POST)

        if form_patient.is_valid():
            patient = form_patient.save()

            # Préparer les données du mail
            subject = 'Confirmation de l\'ajout du patient'
            message = f'Patient ajouté : {patient.nom_patient}, {patient.prenom_patient}, {patient.password_patient}'  # Ajoutez ici les détails que vous voulez
            recipient = form_patient.cleaned_data.get('mail_patient')  # Assurez-vous que votre formulaire a un champ pour l'e-mail
            print(recipient)

            send_mail_with_mailgun(subject, message, recipient)
            
            return redirect('validation_ajout_patient')
        else:
            pass
    else:
        # Initialiser le formulaire avec les valeurs par défaut
        random_password = generate_random_password()
        initial_values = {
            'fk_id_medecin': Medecin.objects.get(id_medecin=id_medecin_connecte),
            'fk_nom_medecin':  Medecin.objects.get(nom_medecin=nom_medecin_connecte),
            'password_patient': random_password,
        }
        form_patient = PatientForm(initial=initial_values)


    context = {
        'nom_medecin': nom_medecin_connecte, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin_connecte':id_medecin_connecte,
        'form_patient':form_patient
    }

    return render(request, 'ajout_patient.html', context)






# -------------------------------------------------------------------------------------------- Page resultat étude
@custom_login_required_medecin
def resultat_etude(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin = request.session.get('id_medecin', '')
    # --------------------------------------------

    context = {
        'nom_medecin': nom_medecin, 
        'prenom_medecin': prenom_medecin, 
        'id_medecin':id_medecin
    }

    return render(request, 'resultat_etude.html', context)



# -------------------------------------------------------------------------------------------- Page de validation après une correction de compte medecin
@custom_login_required_medecin # décorateur custom pour bloquer l'accés sans séssion
def validation_correction_compte_medecin(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

        
    context = {
        'nom_medecin':nom_medecin,
        'prenom_medecin':prenom_medecin,
        'id_medecin_connecte':id_medecin_connecte
    }
    return render(request, 'validation_correction_compte_medecin.html', context)






# -------------------------------------------------------------------------------------------- Page de validation après ajout d'un patient
@custom_login_required_medecin # décorateur custom pour bloquer l'accés sans séssion
def validation_ajout_patient(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_medecin = request.session.get('nom_medecin', '')
    prenom_medecin = request.session.get('prenom_medecin', '')
    id_medecin_connecte = request.session.get('id_medecin', '')
    # --------------------------------------------

        
    context = {
        'nom_medecin':nom_medecin,
        'prenom_medecin':prenom_medecin,
        'id_medecin_connecte':id_medecin_connecte
    }
    return render(request, 'validation_ajout_patient.html', context)