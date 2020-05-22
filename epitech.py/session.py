import requests

def create(link):
    session = requests.Session()
    session.get(link)
    return (session)