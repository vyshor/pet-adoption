import os
import logging
from users import User
from firebase_admin import credentials, firestore, initialize_app

log = logging.getLogger('db')
# Initialize Firestore DB
cred = credentials.Certificate('servicekey.json')
default_app = initialize_app(cred)
db = firestore.client()
users_db = db.collection('users')
listings_db = db.collection('listings')

# Database structure
#
# db.collection('users')
#   email [String]
# 	profile - JSON object
#       name [String]
#       contact_number [String]
# 	listings - list of listing_id

#
# db.collection('listings')
#   listing_id [String]
#   name [String]
#   animal [String]
#   breed [String]
#   DOB [Unix timestamp - int]
#   img_url [String]
#   description_of_pet [String]
#   pets_owner_email [String]


def create_user(user):
    try:
        res = users_db.document(user.email).set(user.to_firestore())
        log.info(res.update_time)
        return True
    except Exception as e:
        log.error(e)
        return False


def get_user(email):
    try:
        user = users_db.document(email).get()
        if user.exists:
            return User.from_firestore(email, user.to_dict())
        return None
    except Exception as e:
        log.error(e)
        return None


def update_user(user_email, user_details):
    try:
        users_db.document(user_email).update(user_details)
        return True
    except Exception as e:
        print(f"An Error Occured: {e}")


def delete_user(user_email):
    try:
        users_db.document(user_email).delete()
        return True
    except Exception as e:
        log.error(e)
        return False


def get_listings():
    listings = listings_db.stream()

    return [l.to_dict() for l in listings]
    