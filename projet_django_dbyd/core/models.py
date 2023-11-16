from django.db import models

class ActivitePhysique(models.Model):
    OUI_NON_CHOICES = [
        (1, 'Oui'),
        (0, 'Non'),
        # etc.
    ]

    id_activite_physique = models.AutoField(primary_key=True)
    activite_physique_journee_en_cours = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    nature_activite_physique = models.CharField(max_length=300, blank=True, null=True)
    duree_activite_physique_en_min = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'activite_physique'


class Administrator(models.Model):
    id_administrator = models.IntegerField(primary_key=True)  # The composite primary key (id_administrator, nom_administrator) found, that is not supported. The first column is selected.
    nom_administrator = models.CharField(max_length=30, unique=True)
    prenom_administrator = models.CharField(max_length=30, blank=True, null=True)
    password_administrator = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'administrator'
        unique_together = (('id_administrator', 'nom_administrator'),)


class Alimentation(models.Model):
    OUI_NON_CHOICES = [
        (1, 'Oui'),
        (0, 'Non'),
        # etc.
    ]

    id_alimentation = models.AutoField(primary_key=True)
    consommation_alcool = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    grignotage_sale = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    grignotage_sucre = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    nb_repas_journee_en_cours = models.IntegerField(blank=True, null=True)
    quantite_eau_bu = models.FloatField(blank=True, null=True)
    quantite_alcool_bu = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'alimentation'


class AutreSymptome(models.Model):
    OUI_NON_CHOICES = [
        (1, 'Oui'),
        (0, 'Non'),
        # etc.
    ]

    id_autre_symptome = models.AutoField(primary_key=True)
    dyspnee = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    oedeme = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    episode_infectieux = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    fievre = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    palpitation = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    debut_palpitation = models.TimeField(blank=True, null=True)
    duree_palpitation_en_min = models.IntegerField(blank=True, null=True)
    douleur_thoracique = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    debut_douleur_thoracique = models.TimeField(blank=True, null=True)
    duree_douleur_thoracique_en_min = models.IntegerField(blank=True, null=True)
    malaise = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    debut_malaise = models.TimeField(blank=True, null=True)
    duree_malaise_en_min = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'autre_symptome'


class EvaluationNiveauStress(models.Model):
    CHOICES = [
        (0, 'n’est pas apparu'),
        (1, 'apparu une ou deux fois seulement'),
        (5, 'est apparu plusieurs fois'),
        (10, 'est apparu presque continuellement'),
        # etc.
    ]

    id_evaluation_niveau_stress = models.AutoField(primary_key=True)
    irritabilite = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_depressif = models.IntegerField(choices=CHOICES, blank=True, null=True)
    bouche_gorge_seche = models.IntegerField(choices=CHOICES, blank=True, null=True)
    action_geste_impulsif = models.IntegerField(choices=CHOICES, blank=True, null=True)
    grincement_des_dents = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_a_rester_assis = models.IntegerField(choices=CHOICES, blank=True, null=True)
    cauchermars = models.IntegerField(choices=CHOICES, blank=True, null=True)
    diarrhee = models.IntegerField(choices=CHOICES, blank=True, null=True)
    attaque_verbale = models.IntegerField(choices=CHOICES, blank=True, null=True)
    haut_bas_emotif = models.IntegerField(choices=CHOICES, blank=True, null=True)
    grande_envie_de_pleurer = models.IntegerField(choices=CHOICES, blank=True, null=True)
    grande_envie_de_fuir = models.IntegerField(choices=CHOICES, blank=True, null=True)
    grande_envie_de_faire_mal = models.IntegerField(choices=CHOICES, blank=True, null=True)
    pensees_embrouillees = models.IntegerField(choices=CHOICES, blank=True, null=True)
    debit_plus_rapide = models.IntegerField(choices=CHOICES, blank=True, null=True)
    fatigue_ou_lourdeur_generalise = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_de_etre_surchager = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_de_etre_emotivement_fragile = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_de_tristesse = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_de_anxiete = models.IntegerField(choices=CHOICES, blank=True, null=True)
    tension_emotionnelle = models.IntegerField(choices=CHOICES, blank=True, null=True)
    hostilite_envers_les_autres = models.IntegerField(choices=CHOICES, blank=True, null=True)
    tremblement_ou_geste_nerveux = models.IntegerField(choices=CHOICES, blank=True, null=True)
    begaiement_ou_hesitation_verbale = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_incapacite_concentration = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_organiser_pensee = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_dormir = models.IntegerField(choices=CHOICES, blank=True, null=True)
    besoin_frequent_uriner = models.IntegerField(choices=CHOICES, blank=True, null=True)
    maux_estomac = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_digerer = models.IntegerField(choices=CHOICES, blank=True, null=True)
    geste_ou_sentiment_imaptience = models.IntegerField(choices=CHOICES, blank=True, null=True)
    maux_de_tete = models.IntegerField(choices=CHOICES, blank=True, null=True)
    douleur_dos_nuque = models.IntegerField(choices=CHOICES, blank=True, null=True)
    perte_gain_appetit = models.IntegerField(choices=CHOICES, blank=True, null=True)
    perte_interet_sexe = models.IntegerField(choices=CHOICES, blank=True, null=True)
    oublis_frequents = models.IntegerField(choices=CHOICES, blank=True, null=True)
    douleur_serrement_poitrine = models.IntegerField(choices=CHOICES, blank=True, null=True)
    conflit_avec_les_autres = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_a_se_lever_post_sommeil = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sentiment_hors_de_controle = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_activite_longue_continue = models.IntegerField(choices=CHOICES, blank=True, null=True)
    mouvement_retrait_isolement = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_endormissement = models.IntegerField(choices=CHOICES, blank=True, null=True)
    difficulte_post_contrariete = models.IntegerField(choices=CHOICES, blank=True, null=True)
    main_moite = models.IntegerField(choices=CHOICES, blank=True, null=True)
    impact_stress = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'evaluation_niveau_stress'


class InformationCardiaque(models.Model):
    id_information_cardiaque = models.AutoField(primary_key=True)
    frequence_cardiaque_par_min = models.FloatField(blank=True, null=True)
    ta_systolique_matin = models.FloatField(blank=True, null=True)
    ta_systolique_soir = models.FloatField(blank=True, null=True)
    ta_diastolique_matin = models.FloatField(blank=True, null=True)
    ta_diastolique_soir = models.FloatField(blank=True, null=True)
    symptome_cardiovasculaire = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'information_cardiaque'


class Medecin(models.Model):
    id_medecin = models.IntegerField(primary_key=True)  # The composite primary key (id_medecin, nom_medecin) found, that is not supported. The first column is selected.
    nom_medecin = models.CharField(max_length=30, unique=True)
    prenom_medecin = models.CharField(max_length=30, blank=True, null=True)
    mail_medecin = models.CharField(max_length=50, blank=True, null=True)
    password_medecin = models.CharField(max_length=10, blank=True, null=True)
    tel_medecin = models.IntegerField(blank=True, null=True)
    specialite_medecin = models.CharField(max_length=30, blank=True, null=True)
    fk_nom_administrator = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='fk_nom_administrator', to_field='nom_administrator', blank=True, null=True)
    fk_id_administrator = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='fk_id_administrator', related_name='medecin_fk_id_administrator_set', blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'medecin'
        unique_together = (('id_medecin', 'nom_medecin'),)


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)  # The composite primary key (id_patient, nom_patient) found, that is not supported. The first column is selected.
    nom_patient = models.CharField(max_length=30)
    prenom_patient = models.CharField(max_length=30, blank=True, null=True)
    mail_patient = models.CharField(max_length=50, blank=True, null=True)
    password_patient = models.CharField(max_length=10, blank=True, null=True)
    age_patient = models.IntegerField(blank=True, null=True)
    ville_patient = models.CharField(max_length=100, blank=True, null=True)
    tel_patient = models.IntegerField(blank=True, null=True)
    sexe_patient = models.CharField(max_length=50, blank=True, null=True)
    taille_patient = models.IntegerField(blank=True, null=True)
    fk_id_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='fk_id_medecin', blank=True, null=True)
    fk_nom_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='fk_nom_medecin', to_field='nom_medecin', related_name='patient_fk_nom_medecin_set', blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'patient'
        unique_together = (('id_patient', 'nom_patient'),)


class Physique(models.Model):
    id_physique = models.AutoField(primary_key=True)
    poids = models.FloatField(blank=True, null=True)
    tour_de_taille_cm = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'physique'


class PriseMedicament(models.Model):

    OUI_NON_CHOICES = [
        (1, 'Oui'),
        (0, 'Non'),
        # etc.
    ]

    id_prise_medicament = models.AutoField(primary_key=True)
    nb_medicament_pris_dans_la_journee = models.IntegerField(blank=True, null=True)
    oublie_medic_matin = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    oublie_medic_soir = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    effet_secondaire = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    symptome_particulier = models.IntegerField(choices=OUI_NON_CHOICES, blank=True, null=True)
    effet_secondaire_ou_symptome_description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'prise_medicament'


class Reponse(models.Model):
    id_reponse = models.AutoField(primary_key=True)
    date_reponse = models.DateField(blank=True, null=True)
    fk_utilisateur = models.ForeignKey(Patient, models.DO_NOTHING, db_column='fk_utilisateur', blank=True, null=True)
    fk_physique = models.ForeignKey(Physique, models.DO_NOTHING, db_column='fk_physique', blank=True, null=True)
    fk_information_cardiaque = models.ForeignKey(InformationCardiaque, models.DO_NOTHING, db_column='fk_information_cardiaque', blank=True, null=True)
    fk_prise_medicament = models.ForeignKey(PriseMedicament, models.DO_NOTHING, db_column='fk_prise_medicament', blank=True, null=True)
    fk_alimentation = models.ForeignKey(Alimentation, models.DO_NOTHING, db_column='fk_alimentation', blank=True, null=True)
    fk_activite_physique = models.ForeignKey(ActivitePhysique, models.DO_NOTHING, db_column='fk_activite_physique', blank=True, null=True)
    fk_autre_symptome = models.ForeignKey(AutreSymptome, models.DO_NOTHING, db_column='fk_autre_symptome', blank=True, null=True)
    fk_evaluation_niveau_stress = models.ForeignKey(EvaluationNiveauStress, models.DO_NOTHING, db_column='fk_evaluation_niveau_stress', blank=True, null=True)

    class Meta:
        db_table = 'reponse'