import os
import json
import threading
from google.cloud import firestore
from google.oauth2 import service_account

class ApiSeiketsu:
    def __init__(self):
        credentials_file  = os.path.join(os.path.dirname(__file__), 'data', 'firebase_credentials.json')

        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.db = firestore.Client(credentials=credentials, project=credentials.project_id)
        self.new_message_event = threading.Event()

    def _listen_for_changes(self):
        messages_ref = self.db.collection('messages')
        query = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING)

        def on_snapshot(doc_snapshot, changes, read_time):
            self.new_message_event.set()

        query.on_snapshot(on_snapshot)

    def read_message(self):
        self._listen_for_changes()

        while True:
            self.new_message_event.wait()
            messages_ref = self.db.collection('messages')
            docs = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()

            latest_message = None
            for doc in docs:
                latest_message = doc.to_dict()

            self.new_message_event.clear()

    def write_message(self, alias, message_text):
        messages_ref = self.db.collection('messages')
        messages_ref.add({
            'alias': alias + '#BOT',
            'text': message_text,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
