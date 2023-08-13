# api_seiketsu.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Load your Firebase config from the external JSON file
with open('firebase_config.json', 'r') as f:
    firebase_config = json.load(f)

# Initialize Firebase
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)

db = firestore.client()

def read_messages():
    messages_ref = db.collection(u'messages')
    docs = messages_ref.stream()

    messages = []
    for doc in docs:
        messages.append(doc.to_dict())

    return messages

def write_message(alias, message_text):
    messages_ref = db.collection(u'messages')
    messages_ref.add({
        u'alias': alias,
        u'text': message_text,
        u'timestamp': firestore.SERVER_TIMESTAMP,
    })
