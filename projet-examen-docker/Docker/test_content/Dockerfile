# Utiliser l'image Jupyter minimal notebook comme base
FROM jupyter/minimal-notebook:x86_64-python-3.11.6

# Copier le script de test dans le conteneur
COPY test_content.py /app/

# Définir /app comme répertoire de travail
WORKDIR /app

# Installer les dépendances s'il y en a
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour exécuter le script
CMD ["python", "/app/test_content.py"]
