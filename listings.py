import json

# TODO implement
class Listing():
    def __init__(self):
        pass

    @staticmethod
    def from_firestore(source):
        pass

    def to_firestore(self):
        pass
    
    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)
