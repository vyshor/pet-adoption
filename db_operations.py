import os
from firebase_admin import credentials, firestore, initialize_app

print(os.getcwd())
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
#   animal [String]
#   breed [String]
#   DOB [Unix timestamp - int]
#   img_url [String]


def create_user():
    try:
        email = "test@test.com"
        new_user = {
            "profile": {
                "name": "test",
                "contact_number": "12345678"
            },
            "listings": []
        }
        print(users_db.document(email).set(new_user))
        return True
    except Exception as e:
        print(f"An Error Occured: {e}")
        return False


def read_user(user_email):
    try:
        if users_db:
            user_details = users_db.document(user_email).get()
            print(user_details)
            return True
        else:
            print("No DB found")
            return False
    except Exception as e:
        print(f"An Error Occured: {e}")
        return False


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
        print(f"An Error Occured: {e}")
        return False
