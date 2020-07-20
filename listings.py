import json
from db_operations import create_empty_listing

class Listing():
    def __init__(self, animal, breed, dob, description, img_url, user_email, listing_id=''):
        self.listing_id = listing_id
        self.animal = animal
        self.breed = breed
        self.dob = dob
        self.description = description
        self.img_url = img_url
        self.user_email = user_email

        # Listing_id is the document id when uploaded into firebase
        # Thus, it is automatically generated once it is uploaded
        if not listing_id:
            self.listing_id = create_empty_listing()

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