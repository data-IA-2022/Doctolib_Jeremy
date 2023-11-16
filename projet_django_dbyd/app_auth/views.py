from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import check_password
from core.models import Administrator, Reponse, Patient, Medecin
import datetime

@never_cache
def connexion(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')

        user = authenticate(request, nom=nom, prenom=prenom, password=password)
        if user is not None:
            login(request, user)

            # Redirigez en fonction du type d'utilisateur
            if getattr(user, 'user_type', None) == 'patient':
                mois_en_cours = datetime.date.today().month

                # On créer un objet patient avec la table Patient quand ça correspond au nom prenom données dans le formulaire
                patient = Patient.objects.get(nom_patient=nom, prenom_patient=prenom)
                request.session['nom_patient'] = patient.nom_patient
                request.session['prenom_patient'] = patient.prenom_patient
                request.session['id_patient'] = patient.id_patient
                
                # Récupérez la date de la dernière réponse soumise par l'utilisateur connecté pour gérer la périodicité
                try:
                    # Récupérez les réponses soumises par l'utilisateur connecté
                    toute_les_reponses = Reponse.objects.filter(fk_utilisateur=patient.id_patient)
                    mois_derniere_reponse = toute_les_reponses.latest('date_reponse').date_reponse.month if toute_les_reponses else None

                except Reponse.DoesNotExist:
                    mois_derniere_reponse = None
                if mois_derniere_reponse == mois_en_cours:
                    return redirect('formulaire_deja_rempli')  # Redirigez vers la page de décompte
                else:
                    return redirect('patient')  # Redirigez vers la page de soumission du formulaire
                
            elif getattr(user, 'user_type', None) == 'medecin':
                medecin = Medecin.objects.get(nom_medecin=nom, prenom_medecin=prenom)
                request.session['nom_medecin'] = medecin.nom_medecin
                request.session['prenom_medecin'] = medecin.prenom_medecin
                request.session['id_medecin'] = medecin.id_medecin

                return redirect('medecin')
            
            else:
                messages.error(request, 'Erreur lors de la redirection.')
        else:
            messages.error(request, 'Nom, prénom ou mot de passe incorrect.')

    return render(request, 'connexion.html')

@never_cache
def connexion_admin(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')

        try:
            admin = Administrator.objects.get(nom_administrator=nom, prenom_administrator=prenom)
            if check_password(password, admin.password_administrator):
                # Le mot de passe correspond
                # Vous pouvez maintenant utiliser la méthode login pour connecter l'administrateur
                request.session['nom_administrator'] = admin.nom_administrator
                request.session['prenom_administrator'] = admin.prenom_administrator
                request.session['id_administrator'] = admin.id_administrator
                login(request, admin)
                return redirect('administrateur')
            else:
                messages.error(request, 'Mot de passe incorrect pour l\'administrateur.')
        except Administrator.DoesNotExist:
            messages.error(request, 'L\'administrateur n\'existe pas.')

    return render(request, 'connexion_admin.html')