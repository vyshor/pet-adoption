import json

class Listing():
    def __init__(self, pet_name, animal, breed, dob, description, img_url, user_email, listing_id):
        self.listing_id = listing_id
        self.pet_name = pet_name
        self.animal = animal
        self.breed = breed
        self.dob = dob
        self.description = description
        self.img_url = img_url
        self.user_email = user_email

    @staticmethod
    def from_firestore(listing_id, source):
        return Listing(source['pet_name'], source['animal'], source['breed'], source['dob'], source['description_of_pet'], source['img_url'], source['user_email'], listing_id)

    def to_firestore(self):
        return {
            "animal": self.animal,
            "pet_name": self.pet_name,
            "breed": self.breed,
            "dob": self.dob,
            "img_url": self.img_url,
            "user_email": self.user_email,
            "description_of_pet": self.description
        }
    
    def to_json(self):
        return json.dumps(self, default = lambda o: o.__dict__)


