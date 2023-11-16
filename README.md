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

### Étape 2 : Configuration de MySQL

1. Ouvrez Docker et exécutez la commande suivante pour télécharger l'image MySQL :
   ```bash
   docker pull mysql```

   docker run --name nom_conteneur_mysql -e MYSQL_ROOT_PASSWORD=votre_mot_de_passe -d mysql
