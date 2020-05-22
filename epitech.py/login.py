import requests

class login:
    url          = "https://intra.epitech.eu/login?format=json"
    data         = None
    login        = None
    message      = None
    access_token = None

def load(session):
    result = session.get(login.url)
    data = result.json()

    login.data         = data
    login.login        = data['login']
    login.message      = data['message']
    login.access_token = data['access_token']

def search(item):
    try:
        item = login.data["%s" % item]
        return (item)
    except:
        print("Item: '%s' not found" % item)
