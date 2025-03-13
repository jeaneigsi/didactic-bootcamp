# Spécifications de la Base de Données

## Modèle Conceptuel de Données (MCD)

### Entités Principales et Attributs

#### User
- **id**
- **nom**
- **prenom**
- **email**
- **mot_de_passe**  
  Stocké de manière hashée via la méthode Django recommandée.
- **role**  
  Exemples : "Admin", "User". Permet de gérer des rôles spécifiques pour l’affichage de certains boutons.

#### Parcelle
- **id**
- **prix**
- **categorie**  
  Exemple : type de vente, type de bien, etc.
- **description**  
  Permet d'ajouter des informations complémentaires (superficie, type de terrain, etc.).
- **created_at / updated_at**  
  Pour le suivi de la publication.

**Relations :**
- Appartient à un **User** (lorsqu’un utilisateur poste une annonce).
- Est localisée dans une **Ville/Quartier**.

#### Ville/Quartier
- **id**
- **nom**  
  Exemple : quartiers de Casablanca comme "Maarif", "Sidi Moumen", etc.

#### Favoris (ou Sauvegarde de Parcelles)
- **id**
- **created_at**  
  (Optionnel, pour savoir quand l’utilisateur a sauvegardé la parcelle.)

**Relations :**
- Lien **Many-to-Many** entre **User** et **Parcelle** :
  - Un **User** peut avoir plusieurs parcelles favorites.
  - Une **Parcelle** peut être sauvegardée par plusieurs utilisateurs.

### Relations Globales
- **User → Parcelle** :  
  Un utilisateur (ayant posté une annonce) peut poster plusieurs parcelles, tandis qu’une parcelle est postée par un seul utilisateur.
- **Parcelle → Ville/Quartier** :  
  Une parcelle est associée à un quartier (ou une ville) de Casablanca.
- **User ↔ Parcelle (Favoris)** :  
  Relation many-to-many pour la sauvegarde des annonces.
