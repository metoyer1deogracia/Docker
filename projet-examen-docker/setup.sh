#!/bin/bash

# Construire les images Docker spécifiées dans le fichier docker-compose.yml
echo "Construire les images Docker spécifiées dans le fichier docker-compose.yml"
docker-compose build

# Démarrer les conteneurs Docker spécifiés dans le fichier docker-compose.yml
echo "Démarrer les conteneurs Docker spécifiés dans le fichier docker-compose.yml"
docker-compose up -d

# Afficher les conteneurs Docker en cours d'exécution
echo "Afficher les conteneurs Docker en cours d'exécution"
docker ps

# Attendre que les tests soient terminés (ajustez selon le temps d'exécution attendu des tests)
echo "Attente pour la fin des tests..."
sleep 10  # Ajustez cette valeur selon le besoin

