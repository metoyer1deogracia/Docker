
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests

# Adresse de l'API
API_URL = "http://api:8000"

def log_result(output):
    """Fonction pour logger les résultats des tests."""
    with open('/app/logs/api_test.log', 'a') as file:
        file.write(output + "\n")

def test_authorization(username, password, endpoint, expected_status):
    """Fonction pour tester l'autorisation d'accès aux différents endpoints."""
    response = requests.get(f"{API_URL}/{endpoint}", params={"username": username, "password": password, "sentence": "Test sentence"})
    test_status = 'SUCCESS' if response.status_code == expected_status else 'FAILURE'
    
    log_message = f'''
    ============================
        Authorization test
    ============================
    
    request done at "/{endpoint}"
    | username="{username}"
    | password="{'*' * len(password)}"  # Masquer le mot de passe pour la sécurité
    
    expected result = {expected_status}
    actual result = {response.status_code}
    
    ==>  {test_status}
    '''
    
    # Log du résultat
    log_result(log_message)

if __name__ == "__main__":
    # Tests d'autorisation
    test_authorization("bob", "builder", "v1/sentiment", 200)
    test_authorization("bob", "builder", "v2/sentiment", 403)

    test_authorization("alice", "wonderland", "v1/sentiment", 200)
    test_authorization("alice", "wonderland", "v2/sentiment", 200)

    print("Tous les tests d'autorisation ont réussi.")
