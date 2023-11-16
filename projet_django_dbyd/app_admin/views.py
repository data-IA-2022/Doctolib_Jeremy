from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from core.custom_decorators import custom_login_required_admin

@custom_login_required_admin
def administrateur(request):
    # --------------------------------------------
    # Affichage de l'entête avec le nom/prenom/id
    nom_administrator = request.session.get('nom_administrator', '')
    prenom_administrator = request.session.get('prenom_administrator', '')
    id_admin_connecte = request.session.get('id_administrator', '')
    # --------------------------------------------

    print ("---------------------------------------------- RAPPORT ADMINISTRATEUR ----------------------------------------------")
    if 'nom_administrator' in request.session and 'prenom_administrator' in request.session:
        print("Session existante dans la page administration :")
        print("Nom de l'admin :", request.session['nom_administrator'])
        print("Prénom de l'admin :", request.session['prenom_administrator'])
    else:
        print("Aucune session active.")
    print ("--------------------------------------------------------------------------------------------------------------------")


    hashed_password = ""
    if request.method == "POST":
        plain_password = request.POST.get('password')
        hashed_password = make_password(plain_password)


    context = {
        'nom_administrator':nom_administrator,
        'prenom_administrator':prenom_administrator,
        'id_admin_connecte':id_admin_connecte,
        'hashed_password': hashed_password
    }
    return render(request, 'administrateur.html', context)

def generer_mdp(request):
    hashed_password = ""
    if request.method == "POST":
        plain_password = request.POST.get('password')
        hashed_password = make_password(plain_password)

    return render(request, 'generer_mdp.html', {'hashed_password': hashed_password})