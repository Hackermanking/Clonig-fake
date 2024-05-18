from fbchat import Client
from fbchat.models import *
import getpass

# Demande les informations de connexion à l'utilisateur
username = input("Entrez votre numéro de téléphone ou adresse e-mail : ")
password = getpass.getpass("Entrez votre mot de passe : ")

# Connexion à Facebook
class CustomClient(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        print("Message reçu de {}: {}".format(author_id, message_object.text))

client = CustomClient(username, password)
print("Connecté avec succès à Facebook.")

def afficher_messages():
    messages = client.fetchThreadMessages(thread_id=client.uid, limit=10)
    messages.reverse()  # Pour afficher du plus ancien au plus récent
    for message in messages:
        auteur = client.fetchUserInfo(message.author)[message.author]
        print("{} a dit : {}".format(auteur.name, message.text))

def afficher_profil():
    profil = client.fetchProfile(client.uid)
    print("Nom: ", profil.name)
    print("Email: ", profil.email)
    print("Numéro de téléphone: ", profil.phone)
    print("Adresse: ", profil.address)

def afficher_parametres():
    print("Les paramètres du compte ne sont pas encore implémentés.")

# Menu interactif
while True:
    print("\nChoisissez une option :")
    print("1. Voir les messages")
    print("2. Paramètres du compte")
    print("3. Profil")
    print("4. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == '1':
        afficher_messages()
    elif choix == '2':
        afficher_parametres()
    elif choix == '3':
        afficher_profil()
    elif choix == '4':
        print("Déconnexion...")
        client.logout()
        break
    else:
        print("Choix invalide. Veuillez réessayer.")