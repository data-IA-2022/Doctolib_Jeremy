import secrets
import string

# Fonction pour générer un mot de passe aléatoire
def generate_random_password(length=9):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))