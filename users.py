import json

class User():
    def __init__(self, email, name, contact_number, listings):
        self.email = email
        self.name = name
        self.contact_number = contact_number
        self.listings = listings

    @staticmethod
    def from_firestore(email, source):
        return User(email, source['profile']['name'], source['profile']['contact_number'], source['listings'])

    def to_firestore(self):
        return {
            "profile": {
                "name": self.name,
                "contact_number": self.contact_number
            },
            "listings": self.listings
        }

    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)
