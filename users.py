import json

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, email: str, name: str, password: str, contact_number: str, listings):
        self.email = email
        self.name = name
        self.password = password
        self.contact_number = contact_number
        self.listings = listings
        # needed for flask-login: see UserMixin impl
        self.id = self.email

    @staticmethod
    def from_firestore(email, source):
        return User(email, source['profile']['name'], source['profile']['hashed_password'], source['profile']['contact_number'], source['listings'])

    def to_firestore(self):
        return {
            "profile": {
                "hashed_password": self.password,
                "name": self.name,
                "contact_number": self.contact_number
            },
            "listings": self.listings
        }

    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)
