from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):

    print ("---------------------------------------------- RAPPORT PAGE D'ACCUEIL ----------------------------------------------")

    if 'nom_patient' in request.session and 'prenom_patient' in request.session:
        print("Session existante :")
        print("Nom du patient :", request.session['nom_patient'])
        print("Prénom du patient :", request.session['prenom_patient'])
    else:
        print("Aucune session patient active.")

    if 'nom_administrator' in request.session and 'prenom_administrator' in request.session:
        print("Session existante :")
        print("Nom de l'admin :", request.session['nom_administrator'])
        print("Prénom de l'admin :", request.session['prenom_administrator'])
    else:
        print("Aucune session admin active.")

    if 'nom_medecin' in request.session and 'prenom_medecin' in request.session:
        print("Session existante :")
        print("Nom du medecin :", request.session['nom_medecin'])
        print("Prénom du medecin :", request.session['prenom_medecin'])
    else:
        print("Aucune session medecin active.")

    print ("--------------------------------------------------------------------------------------------------------------------")

    return render(request, 'index.html')

def deconnexion(request):

    print ("---------------------------------------------- RAPPORT PAGE DECONNEXION --------------------------------------------")

    if 'nom_patient' in request.session and 'prenom_patient' in request.session:
        print("Session existante :")
        print("Nom du patient :", request.session['nom_patient'])
        print("Prénom du patient :", request.session['prenom_patient'])
    else:
        print("Aucune session patient active.")

    if 'nom_administrator' in request.session and 'prenom_administrator' in request.session:
        print("Session existante :")
        print("Nom de l'admin :", request.session['nom_administrator'])
        print("Prénom de l'admin :", request.session['prenom_administrator'])
    else:
        print("Aucune session admin active.")

    if 'nom_medecin' in request.session and 'prenom_medecin' in request.session:
        print("Session existante :")
        print("Nom du medecin :", request.session['nom_medecin'])
        print("Prénom du medecin :", request.session['prenom_medecin'])
    else:
        print("Aucune session medecin active.")

    print ("--------------------------------------------------------------------------------------------------------------------")

    logout(request)

    return render(request, 'deconnexion.html')  # Redirection vers la page de connexion ou la page d'accueil, selon vos besoins.


