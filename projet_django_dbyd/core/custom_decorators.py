from django.shortcuts import redirect

def custom_login_required_admin(function):
    def wrapper(request, *args, **kwargs):
        if 'nom_administrator' in request.session and 'prenom_administrator' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper

def custom_login_required_patient(function):
    def wrapper(request, *args, **kwargs):
        if 'nom_patient' in request.session and 'prenom_patient' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper

def custom_login_required_medecin(function):
    def wrapper(request, *args, **kwargs):
        if 'nom_medecin' in request.session and 'prenom_medecin' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper