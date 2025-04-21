import os
import django
import csv
from django.core.files import File

# Configure Django (Assurez-vous que le chemin vers settings.py est correct)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.module.settings")  # ⚠️ Assurez-vous que le chemin vers settings.py est bon
django.setup()

from annonces.models import User, Ville, Parcelle, Favoris, Panier, PanierItem

def run():
    print("🟢 Début de l'importation des données...")
    
    # Ouvre le fichier CSV avec les données à importer
    with open("backend/data/data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Parcours chaque ligne du CSV
        for row in reader:
            # Créer ou récupérer Ville
            ville, _ = Ville.objects.get_or_create(nom=row['ville'])

            # Créer ou récupérer User
            user, _ = User.objects.get_or_create(
                email=row['email'],
                defaults={
                    'username': row['email'].split('@')[0],
                    'firstname': row['firstname'],
                    'lastname': row['lastname'],
                    'role': row['role'],
                    'password': 'pbkdf2_sha256$260000$fakepasswordhash$justforinitial'  # mot de passe factice
                }
            )

            # Créer Parcelle
            parcelle, _ = Parcelle.objects.get_or_create(
                nom=row['parcelle_nom'],
                defaults={
                    'prix': float(row['prix']),
                    'user': user,
                    'ville': ville,
                    'categorie': row['categorie'],
                    'description': row['description'],
                }
            )

            # Assigner l'image à chaque parcelle (image se trouve dans le dossier media)
            image_path = "backend/media/annonces/images/_image.webp"
            with open(image_path, "rb") as image_file:
                parcelle.image.save("_image.webp", File(image_file), save=True)

            # Créer Favoris si spécifié dans le CSV
            try:
                fav_parcelle = Parcelle.objects.get(nom=row['favoris_parcelle'])
                Favoris.objects.get_or_create(user=user, parcelle=fav_parcelle)
            except Parcelle.DoesNotExist:
                print(f"[!] Parcelle pour favoris non trouvée: {row['favoris_parcelle']}")

            # Créer Panier
            panier, _ = Panier.objects.get_or_create(user=user)

            # Ajouter un item au Panier
            try:
                panier_item_parcelle = Parcelle.objects.get(nom=row['panier_parcelle'])
                PanierItem.objects.get_or_create(panier=panier, parcelle=panier_item_parcelle)
            except Parcelle.DoesNotExist:
                print(f"[!] Parcelle pour panier non trouvée: {row['panier_parcelle']}")

    print("✅ Importation terminée avec succès.")

if __name__ == '__main__':
    run()
