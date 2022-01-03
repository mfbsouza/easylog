from firebase_admin import credentials, firestore, initialize_app

# initialize firestore DB
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()
