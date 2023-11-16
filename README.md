# Doctolib_Jeremy
 
## Description

Une brève description de ce que fait votre application, ses caractéristiques principales, et pourquoi elle est utile ou intéressante.

## Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [DBeaver](https://dbeaver.io/download/)
- DBInspect ou un outil similaire

## Installation et Configuration

### Étape 1 : Installation de Docker Desktop

1. Téléchargez Docker Desktop depuis le lien fourni ci-dessus.
2. Suivez les instructions d'installation pour votre système d'exploitation.

### Étape 2 : Création et Lancement d'un Conteneur MySQL

1. Ouvrez Docker et exécutez la commande suivante pour télécharger l'image MySQL :
   ```bash
   docker pull mysql
   
2. Ou avec docker desktop directement
3. Lancez le conteneur
   ```bash
   docker run --name nom_conteneur_mysql -e MYSQL_ROOT_PASSWORD=root -d mysql

### Étape 3 : Création de la bdd

1. Ouvrez DBeaver et connectez-vous à votre base de données MySQL dans Docker.
   Éléments de connection :
   ```bash
   Server host : 127.0.0.1
   Port : 3306
   Nom d'utilisateur : root
   Mot de passe : root
2. Créer la bdd Doctolib_By_Django
3. Exécutez votre script SQL pour configurer la base de données.

   ```bash
   CREATE TABLE `reponse` (
     `id_reponse` int,
     `date_reponse` date,
     `fk_utilisateur` int,
     `fk_physique` int,
     `fk_information_cardiaque` int,
     `fk_prise_medicament` int,
     `fk_alimentation` int,
     `fk_activite_physique` int,
     `fk_autre_symptome` int,
     `fk_evaluation_niveau_stress` int,
     PRIMARY KEY (`id_reponse`)
   );

   CREATE TABLE `patient` (
     `id_patient` int,
     `nom_patient` varchar(30),
     `prenom_patient` varchar(30),
     `mail_patient` varchar(50),
     `password_patient` varchar(10),
     `age_patient` int,
     `ville_patient` varchar(100),
     `tel_patient` int,
     `sexe_patient` varchar(50),
     `taille_patient` int,
     `fk_id_medecin` int,
     `fk_nom_medecin` varchar(50),
     PRIMARY KEY (`id_patient`, `nom_patient`)
   );
   
   CREATE TABLE `medecin` (
     `id_medecin` int,
     `nom_medecin` varchar(30),
     `prenom_medecin` varchar(30),
     `mail_medecin` varchar(50),
     `password_medecin` varchar(10),
     `tel_medecin` float,
     `specialite_medecin` varchar(30),
     `fk_nom_administrator` varchar(30),
     `fk_id_administrator` int,
     PRIMARY KEY (`id_medecin`, `nom_medecin`)
   );
   
   CREATE TABLE `administrator` (
     `id_administrator` int,
     `nom_administrator` varchar(30),
     `prenom_administrator` varchar(30),
     `password_administrator` varchar(10),
     PRIMARY KEY (`id_administrator`, `nom_administrator`)
   );
   
   CREATE TABLE `physique` (
     `id_physique` int,
     `poids` float,
     `tour_de_taille_cm` float,
     PRIMARY KEY (`id_physique`)
   );
   
   CREATE TABLE `information_cardiaque` (
     `id_information_cardiaque` int,
     `frequence_cardiaque_par_min` float,
     `ta_systolique_matin` float,
     `ta_systolique_soir` float,
     `ta_diastolique_matin` float,
     `ta_diastolique_soir` float,
     `symptome_cardiovasculaire` varchar(300),
     PRIMARY KEY (`id_information_cardiaque`)
   );
   
   CREATE TABLE `prise_medicament` (
     `id_prise_medicament` int,
     `nb_medicament_pris_dans_la_journee` int,
     `oublie_medic_matin` boolean,
     `oublie_medic_soir` boolean,
     `effet_secondaire` boolean,
     `symptome_particulier` boolean,
     `effet_secondaire_ou_symptome_description` varchar(300),
     PRIMARY KEY (`id_prise_medicament`)
   );
   
   CREATE TABLE `alimentation` (
     `id_alimentation` int,
     `consommation_alcool` boolean,
     `grignotage_sale` boolean,
     `grignotage_sucre` boolean,
     `nb_repas_journee_en_cours` int,
     `quantite_eau_bu` float,
     `quantite_alcool_bu` float,
     PRIMARY KEY (`id_alimentation`)
   );
   
   CREATE TABLE `activite_physique` (
     `id_activite_physique` int,
     `activite_physique_journee_en_cours` boolean,
     `nature_activite_physique` varchar(300),
     `duree_activite_physique_en_min` int,
     PRIMARY KEY (`id_activite_physique`)
   );
   
   CREATE TABLE `autre_symptome` (
     `id_autre_symptome` int,
     `dyspnee` boolean,
     `oedeme` boolean,
     `episode_infectieux` boolean,
     `fievre` boolean,
     `palpitation` boolean,
     `debut_palpitation` timestamp,
     `duree_palpitation_en_min` timestamp,
     `douleur_thoracique` boolean,
     `debut_douleur_thoracique` timestamp,
     `duree_douleur_thoracique_en_min` timestamp,
     `malaise` boolean,
     `debut_malaise` timestamp,
     `duree_malaise_en_min` timestamp,
     PRIMARY KEY (`id_autre_symptome`)
   );
   
   CREATE TABLE `evaluation_niveau_stress` (
     `id_evaluation_niveau_stress` int,
     `irritabilite` int,
     `sentiment_depressif` int,
     `bouche_gorge_seche` int,
     `action_geste_impulsif` int,
     `grincement_des_dents` int,
     `difficulte_a_rester_assis` int,
     `cauchermars` int,
     `diarrhee` int,
     `attaque_verbale` int,
     `haut_bas_emotif` int,
     `grande_envie_de_pleurer` int,
     `grande_envie_de_fuir` int,
     `grande_envie_de_faire_mal` int,
     `pensees_embrouillees` int,
     `debit_plus_rapide` int,
     `fatigue_ou_lourdeur_generalise` int,
     `sentiment_de_etre_surchager` int,
     `sentiment_de_etre_emotivement_fragile` int,
     `sentiment_de_tristesse` int,
     `sentiment_de_anxiete` int,
     `tension_emotionnelle` int,
     `hostilite_envers_les_autres` int,
     `tremblement_ou_geste_nerveux` int,
     `begaiement_ou_hesitation_verbale` int,
     `difficulte_incapacite_concentration` int,
     `difficulte_organiser_pensee` int,
     `difficulte_dormir` int,
     `besoin_frequent_uriner` int,
     `maux_estomac` int,
     `difficulte_digerer` int,
     `geste_ou_sentiment_imaptience` int,
     `maux_de_tete` int,
     `douleur_dos_nuque` int,
     `perte_gain_appetit` int,
     `perte_interet_sexe` int,
     `oublis_frequents` int,
     `douleur_serrement_poitrine` int,
     `conflit_avec_les_autres` int,
     `difficulte_a_se_lever_post_sommeil` int,
     `sentiment_hors_de_controle` int,
     `difficulte_activite_longue_continue` int,
     `mouvement_retrait_isolement` int,
     `difficulte_endormissement` int,
     `difficulte_post_contrariete` int,
     `main_moite` int,
     `impact_stress` int,
     PRIMARY KEY (`id_evaluation_niveau_stress`)
   );
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_utilisateur`) REFERENCES `patient` (`id_patient`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_physique`) REFERENCES `physique` (`id_physique`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_information_cardiaque`) REFERENCES `information_cardiaque` (`id_information_cardiaque`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_prise_medicament`) REFERENCES `prise_medicament` (`id_prise_medicament`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_alimentation`) REFERENCES `alimentation` (`id_alimentation`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_activite_physique`) REFERENCES `activite_physique` (`id_activite_physique`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_autre_symptome`) REFERENCES `autre_symptome` (`id_autre_symptome`);
   
   ALTER TABLE `reponse` ADD FOREIGN KEY (`fk_evaluation_niveau_stress`) REFERENCES `evaluation_niveau_stress` (`id_evaluation_niveau_stress`);
   
   ALTER TABLE `patient` ADD FOREIGN KEY (`fk_id_medecin`, `fk_nom_medecin`) REFERENCES `medecin` (`id_medecin`, `nom_medecin`);
   
   ALTER TABLE `medecin` ADD FOREIGN KEY (`fk_id_administrator`, `fk_nom_administrator`) REFERENCES `administrator` (`id_administrator`, `nom_administrator`);
  
4. Créer la connection avec django dans settings.py
   ```bash
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'doctolib_by_django_donnee_test',
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   
 5. Vérifier avec la commande
   ```bash
   dbinspect
