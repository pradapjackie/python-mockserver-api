import requests

def fetch_external_data():
    response = requests.get("https://api.external-service.com/data")
    return response.json()