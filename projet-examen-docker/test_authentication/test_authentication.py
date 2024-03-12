#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests

# Configuration initiale
API_URL = os.getenv("API_URL", "http://api:8000")


def log_result(output):
    """Fonction pour logger les résultats des tests dans un fichier ou les afficher."""
    with open('/app/logs/api_test.log', 'a', encoding='utf-8') as file:
        file.write(output + "\n")

def test_authentication(username, password, expected_status):
    """
    Teste l'authentification et enregistre le résultat.
    Effectue une requête GET sur le point d'entrée /permissions.
    """
    response = requests.get(f"{API_URL}/permissions", params={"username": username, "password": password})
    test_status = 'SUCCESS' if response.status_code == expected_status else 'FAILURE'
    
    log_message = (
        f"Authentication test:\n"
        f"Request: /permissions | username='{username}', password='{'*' * len(password)}'\n"
        f"Expected result: {expected_status}, Actual result: {response.status_code}\n"
        f"Test: {test_status}\n"
    )
    
    log_result(log_message)
    
    assert response.status_code == expected_status, f"Échec du test d'authentification pour {username} avec le mot de passe {password}. Attendu: {expected_status}, obtenu: {response.status_code}"
    

if __name__ == "__main__":
    test_authentication("alice", "wonderland", 200)
    test_authentication("bob", "builder", 200)
    test_authentication("clementine", "mandarine", 403)

    print("Tous les tests d'authentification ont été exécutés.")
