from django.urls import path
from . import views

urlpatterns = [
    path('administrateur', views.administrateur, name='administrateur'),
    path('administrateur/generer_mdp', views.generer_mdp, name='generer_mdp'),
]