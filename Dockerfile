# Utiliser une image de base officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 8000

# Définir la commande pour exécuter l'application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "src.app:app"]
