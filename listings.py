import json

class Listing():
    def __init__(self, listing_id, animal, breed, dob, img_url, user_email):
        self.listing_id = listing_id
        self.animal = animal
        self.breed = breed
        self.dob = dob
        self.img_url = img_url
        self.user_email = user_email

    @staticmethod
    def from_firestore(listing_id, source):
        return Listing(listing_id, source['animal'], source['breed'], source['dob'], source['img_url'], source['user_email'])

    def to_firestore(self):
        return {
            "animal": self.animal,
            "breed": self.breed,
            "dob": self.dob,
            "img_url": self.img_url,
            "user_email": self.user_email
        }
    
    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)