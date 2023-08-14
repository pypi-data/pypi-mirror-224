import os
import json
from google.cloud import firestore
from google.oauth2 import service_account

class ApiSeiketsu:
    def __init__(self):
        credentials_file  = os.path.join(os.path.dirname(__file__), 'data', 'firebase_credentials.json')

        if not credentials_file:
            raise Exception("JSON credentials file not found in the project directory")

        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.db = firestore.Client(credentials=credentials, project=credentials.project_id)

    def read_latest_message(self):
        messages_ref = self.db.collection('messages')
        docs = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()

        latest_message = None
        for doc in docs:
            latest_message = doc.to_dict()

        return latest_message

    def write_message(self, alias, message_text):
        messages_ref = self.db.collection('messages')
        messages_ref.add({
            'alias': alias + '#BOT',
            'text': message_text,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
