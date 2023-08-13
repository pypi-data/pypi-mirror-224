import os
from google.cloud import firestore
from google.oauth2 import service_account

# Search for the first file with ".json" extension in the project directory
credentials_file = next((file for file in os.listdir('.') if file.endswith('.json')), None)

if not credentials_file:
    raise Exception("JSON credentials file not found in the project directory")

# Load the credentials file and create a Firestore client
credentials = service_account.Credentials.from_service_account_file(credentials_file)
db = firestore.Client(credentials=credentials, project=credentials.project_id)

def read_message():
    # Read the latest message from Firestore
    messages_ref = db.collection('messages')
    docs = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()

    latest_message = None

    for doc in docs:
        latest_message = doc.to_dict()

    return latest_message

def write_message(alias, message_text):
    # Write the message to Firestore
    messages_ref = db.collection('messages')
    messages_ref.add({
        'alias': alias,
        'text': message_text + '1234',
        'timestamp': firestore.SERVER_TIMESTAMP
    })
