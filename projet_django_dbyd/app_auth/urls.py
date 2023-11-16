from django.urls import path
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('connexion_admin', views.connexion_admin, name='connexion_admin'),
]