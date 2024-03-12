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

def test_sentiment_version(username, password, sentence, version, expected_score):
    """Fonction pour tester le sentiment analysis."""
    response = requests.post(f"{API_URL}/{version}/sentiment", json={"username": username, "password": password, "sentence": sentence})
    assert response.status_code == 200, f"Échec de la requête à {version} pour {sentence}"
    data = response.json()
    score = data.get("score")
    assert score == expected_score, f"Échec du test pour {sentence} avec {version}. Attendu: {expected_score}, obtenu: {score}"
    
    # Log du résultat
    log_message = f'''
    ============================
        Content test - {version}
    ============================
    
    request done at "/{version}/sentiment"
    | username="{username}"
    | sentence="{sentence}"
    
    expected score = {expected_score}
    actual score = {score}
    
    ==>  TEST {'SUCCESS' if score == expected_score else 'FAILURE'}
    '''
    log_result(log_message)

if __name__ == "__main__":
    # Test des versions du modèle de sentiment analysis
    test_sentiment_version("alice", "wonderland", "life is beautiful", "v1", 1)
    test_sentiment_version("alice", "wonderland", "that sucks", "v1", -1)
    test_sentiment_version("alice", "wonderland", "life is beautiful", "v2", 1)
    test_sentiment_version("alice", "wonderland", "that sucks", "v2", -1)


    print("Tous les tests de contenu ont réussi.")
