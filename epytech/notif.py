import requests

class init():
    def __init__(self):
        self.data = {
            "url" : "https://intra.epitech.eu/user/notification/alert?format=json"
        }

    def load(self, session):
        result = session.get(self.data.get("url"))
        if result != None:
            self.data = result.json()

    def len(self):
        return (len(self.data))
    
    def data(self):
        return (self.data)

    def search(self, group):
        return (self.data[group].get('title'))