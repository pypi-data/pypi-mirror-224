import json
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "firestore_key.json")
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


def read_last_message():
    messages_ref = db.collection("messages")
    query = messages_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)
    docs = query.get()

    last_message = None

    for doc in docs:
        last_message = {"id": doc.id, "data": doc.to_dict()}

    return last_message


def write_message(alias, message_text):
    messages_ref = db.collection("messages")

    message = {
        "alias": alias,
        "text": message_text,
        "timestamp": firestore.SERVER_TIMESTAMP,
    }

    messages_ref.add(message)
