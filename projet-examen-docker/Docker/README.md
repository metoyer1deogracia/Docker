***Projet Examen Docker***

Ce projet contient des scripts de test pour évaluer une API à l'aide de Docker.

## Introduction

Ce projet vise à automatiser le processus d'évaluation d'une API à l'aide de scripts de test intégrés dans des conteneurs Docker. L'objectif est de garantir le bon fonctionnement de l'API dans différents scénarios et de faciliter le processus de développement en fournissant un environnement de test cohérent et isolé.

## Configuration requise

Assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Docker
- Git (pour cloner ce dépôt)

## Installation

1. Clonez ce dépôt sur votre machine :

```bash
git clone https://github.com/votre-utilisateur/projet-examen-docker.git
cd projet-examen-docker
```


Exécutez le script de configuration setup.sh pour construire les images Docker et démarrer les conteneurs :
./setup.sh

Attendez que les tests soient terminés. Le script attend 10 secondes par défaut.
Consultez les journaux des tests dans le répertoire logs.

***Structure du projet***

## Le projet est structuré comme suit :

docker-compose.yml: Le fichier de configuration Docker Compose décrivant les services et leur configuration.
logs/: Le répertoire où les journaux des tests seront stockés.
setup.sh: Le script de configuration pour construire les images et démarrer les conteneurs.
test_authentication/, test_authorization/, test_content/: Les répertoires contenant les scripts de test pour chaque fonctionnalité de l'API.
Services

## Le projet utilise les services suivants :

api: Le service API basé sur l'image datascientest/fastapi:1.0.0.
test_authentication, test_authorization, test_content: Les services de test pour chaque fonctionnalité de l'API.
Tests

Les tests sont exécutés dans des conteneurs Docker séparés pour chaque fonctionnalité de l'API. Les journaux des tests sont enregistrés dans le répertoire logs pour une analyse ultérieure.

## Contributions

Les contributions sous forme de pull requests sont les bienvenues. Pour des changements majeurs, veuillez d'abord ouvrir une issue pour discuter de ce que vous aimeriez changer.

## Auteurs

METOYER DEO-GRACIA 
Licence

