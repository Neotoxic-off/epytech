import requests

def do(session):
    result = session.get("https://intra.epitech.eu/login?format=json")
    data = result.json()
    return(data)