import os
from google.cloud import firestore
from google.oauth2 import service_account

def _get_firestore_client():
    # Search for the first file with ".json" extension in the project directory
    credentials_file = next((file for file in os.listdir('.') if file.endswith('.json')), None)

    if not credentials_file:
        raise Exception("JSON credentials file not found in the project directory")

    # Load the credentials file and create a Firestore client
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    client = firestore.Client(credentials=credentials, project=credentials.project_id)

    return client

def read_messages():
    db = _get_firestore_client()

    # Read messages from Firestore
    messages_ref = db.collection('messages')
    docs = messages_ref.order_by('timestamp').stream()

    messages = []

    for doc in docs:
        messages.append(doc.to_dict())

    return messages

def write_message(alias, message_text):
    db = _get_firestore_client()

    # Write the message to Firestore
    messages_ref = db.collection('messages')
    messages_ref.add({
        'alias': alias,
        'text': message_text,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
