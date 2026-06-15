import os
import json
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore

cred_json = os.getenv("FIREBASE_CREDENTIALS")
cred_dict = json.loads(cred_json)

cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)

db = firestore.Client()

# Leer (sigue funcionando)
jugadores = db.collection("jugadores").stream()

for doc in jugadores:
    print(doc.id, doc.to_dict())