import os
import json
from google.oauth2 import service_account
from google.cloud import firestore

# Load Firebase configuration from adjacent JSON file
_credentials_file = os.path.join(os.path.dirname(__file__), "firebase_credentials.json")
_credentials_data = None
with open(_credentials_file, "r") as f:
    _credentials_data = json.load(f)

_credentials = service_account.Credentials.from_service_account_info(_credentials_data)
_firestore_client = firestore.Client(credentials=_credentials, project=_credentials_data["project_id"])

def read_messages():
    messages_ref = _firestore_client.collection("messages")
    messages = []
    for doc in messages_ref.stream():
        messages.append(doc.to_dict())
    return messages

def write_message(message_text, alias):
    new_message = {
        "text": message_text,
        "alias": alias,
        "timestamp": firestore.SERVER_TIMESTAMP,
    }
    messages_ref = _firestore_client.collection("messages")
    new_message_ref = messages_ref.add(new_message)
    return new_message_ref[1].id
