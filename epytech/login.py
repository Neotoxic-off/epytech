import requests

class init():
    def __init__(self):
        self.data = {
            "url" : "https://intra.epitech.eu/login?format=json"
        }

    def load(self, session):
        result = session.get(self.data.get("url"))
        if result != None:
            self.data = result.json()

    def search(self, item):
        return (self.data.get(item))
