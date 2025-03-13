### 📌 **Documentation API - Endpoints Disponibles**

Voici la liste des endpoints disponibles pour l’API, à destination de l’équipe frontend développant avec Vue.js.

---

## **🛠 Authentification**
### 🔹 **Obtenir un Token d'authentification**
- **URL** : `POST /api/api-token-auth/`
- **Body (JSON)** :
  ```json
  {
      "username": "votre_email",
      "password": "votre_mot_de_passe"
  }
  ```
- **Réponse (succès)** :
  ```json
  {
      "token": "xxxxxxxxxxxxxxxxxxxx"
  }
  ```
- **Remarque** : Le token doit être ajouté dans les headers pour les requêtes sécurisées :
  ```
  Authorization: Token xxxxxxxxxxxxxxxxxxxx
  ```

---

## **📌 Parcelles**
### 🔹 **Lister toutes les parcelles**
- **URL** : `GET /api/parcelles/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "nom": "Parcelle A",
          "prix": 50000,
          "categorie": "Residentiel",
          "ville": "Dakar",
          "description": "Belle parcelle en centre-ville",
          "image": "url_de_l_image",
          "created_at": "2025-03-12T12:00:00Z"
      }
  ]
  ```

### 🔹 **Créer une nouvelle parcelle**
- **URL** : `POST /api/parcelles/`
- **Headers** : `Authorization: Token {votre_token}`
- **Body (Form-Data ou JSON)** :
  ```json
  {
      "nom": "Parcelle B",
      "prix": 60000,
      "categorie": "Nue",
      "ville": 2,
      "description": "Terrain nu de 500m²",
      "image": "fichier_image"
  }
  ```

### 🔹 **Récupérer une parcelle par ID**
- **URL** : `GET /api/parcelles/{id}/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  {
      "id": 1,
      "nom": "Parcelle A",
      "prix": 50000,
      "categorie": "Residentiel",
      "ville": "Dakar",
      "description": "Belle parcelle en centre-ville",
      "image": "url_de_l_image"
  }
  ```

### 🔹 **Modifier une parcelle (PUT)**
- **URL** : `PUT /api/parcelles/{id}/`
- **Headers** : `Authorization: Token {votre_token}`
- **Body (JSON)** :
  ```json
  {
      "nom": "Parcelle A modifiée",
      "prix": 55000,
      "categorie": "Industriel",
      "ville": 1,
      "description": "Description mise à jour"
  }
  ```

### 🔹 **Supprimer une parcelle**
- **URL** : `DELETE /api/parcelles/{id}/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  {
      "message": "Parcelle supprimée avec succès"
  }
  ```

---

## **📌 Favoris**
### 🔹 **Ajouter une parcelle aux favoris**
- **URL** : `POST /api/favoris/`
- **Headers** : `Authorization: Token {votre_token}`
- **Body (JSON)** :
  ```json
  {
      "parcelle": 1
  }
  ```
- **Réponse** :
  ```json
  {
      "message": "Parcelle ajoutée aux favoris"
  }
  ```

### 🔹 **Lister les favoris d’un utilisateur**
- **URL** : `GET /api/favoris/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "parcelle": {
              "nom": "Parcelle A",
              "prix": 50000
          }
      }
  ]
  ```

### 🔹 **Supprimer un favori**
- **URL** : `DELETE /api/favoris/{id}/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  {
      "message": "Favori supprimé"
  }
  ```

---

## **📌 Panier**
### 🔹 **Récupérer le panier de l’utilisateur**
- **URL** : `GET /api/panier/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  {
      "id": 1,
      "user": "email@exemple.com",
      "parcelles": [
          {
              "id": 3,
              "nom": "Parcelle B",
              "prix": 60000
          }
      ]
  }
  ```

### 🔹 **Ajouter une parcelle au panier**
- **URL** : `POST /api/panier/`
- **Headers** : `Authorization: Token {votre_token}`
- **Body (JSON)** :
  ```json
  {
      "parcelle": 2
  }
  ```

### 🔹 **Supprimer une parcelle du panier**
- **URL** : `DELETE /api/panier/{id}/`
- **Headers** : `Authorization: Token {votre_token}`
- **Réponse** :
  ```json
  {
      "message": "Parcelle retirée du panier"
  }
  ```

---

## **📌 Villes**
### 🔹 **Lister toutes les villes**
- **URL** : `GET /api/villes/`
- **Réponse** :
  ```json
  [
      {"id": 1, "nom": "Dakar"},
      {"id": 2, "nom": "Abidjan"}
  ]
  ```

---

## **✅ Notes importantes**
- **Toutes les routes protégées** nécessitent un **Token d'authentification**.
- **Utiliser les bonnes méthodes HTTP** (`GET`, `POST`, `PUT`, `DELETE`).
- **Tester les endpoints avec Postman** ou `curl`.

🔥 **Bon développement avec Vue.js !** 🚀