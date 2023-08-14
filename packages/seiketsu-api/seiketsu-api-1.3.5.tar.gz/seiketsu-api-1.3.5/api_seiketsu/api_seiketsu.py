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
        self.latest_message = None

        self._listen_for_changes()

    def _listen_for_changes(self):
        messages_ref = self.db.collection('messages')
        query = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING)

        def on_snapshot(doc_snapshot, changes, read_time):
            for change in changes:
                if change.type.name == 'ADDED':
                    self.latest_message = change.document.to_dict()
                    self.new_message_event.set()

        query.on_snapshot(on_snapshot)

    def read_message(self):
        while True:
            self.new_message_event.wait()

            if self.latest_message is not None:
                alias = self.latest_message['alias']
                message_text = self.latest_message['text']

                self.new_message_event.clear()
                return alias, message_text
            else:
                self.new_message_event.clear()

    def write_message(self, alias, message_text):
        messages_ref = self.db.collection('messages')
        messages_ref.add({
            'alias': alias + '#BOT',
            'text': message_text,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
