# Utiliser une image Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de votre projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port que l'application utilise
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]