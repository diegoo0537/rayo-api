"""import os
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)
db = firestore.Client()"""

from google.cloud import firestore

db = firestore.Client()

# Leer (sigue funcionando)
jugadores = db.collection("jugadores").stream()
print(jugadores)