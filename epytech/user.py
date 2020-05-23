import requests

class init():
    def __init__(self):
        self.data = {
            "url" : "https://intra.epitech.eu/user/?format=json"
        }

    def load(self, session):
        result = session.get(self.data.get("url"))
        if result != None:
            self.data = result.json()
    
    def len(self):
        return (len(self.data))
    
    def data(self):
        return (self.data)

    def search(self, item):
        return (self.data.get(item))