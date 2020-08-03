import json

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as TimedSerializer

class User(UserMixin):
    def __init__(self, email: str, name: str, password: str, contact_number: str, verified: bool, listings):
        self.email = email
        self.name = name
        self.password = password
        self.contact_number = contact_number
        self.verified = verified
        self.listings = listings
        # needed for flask-login: see UserMixin impl
        self.id = self.email

    @staticmethod
    def from_firestore(email, source):
        return User(email, source['profile']['name'], source['profile']['hashed_password'], source['profile']['contact_number'], source['profile']['verified'], source['listings'])

    def to_firestore(self):
        return {
            "profile": {
                "hashed_password": self.password,
                "name": self.name,
                "contact_number": self.contact_number,
                "verified": self.verified
            },
            "listings": self.listings
        }

    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)

    def get_token(self, expires_in):
        timed_serializer = TimedSerializer(current_app.config['SECRET_KEY'], expires_in)
        return timed_serializer.dumps({'user_email': self.email}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        timed_serializer = TimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_email = timed_serializer.loads(token)['user_email']
        except:
            return None
        return user_email