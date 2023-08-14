import os
import threading
from google.cloud import firestore
from google.oauth2 import service_account

class ApiSeiketsu:
    def __init__(self):
        credentials_file  = os.path.join(os.path.dirname(__file__), 'data', 'firebase_credentials.json')

        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.db = firestore.Client(credentials=credentials, project=credentials.project_id)
        self.new_message_event = threading.Event()

        self._listen_for_changes()

    def _listen_for_changes(self):
        messages_ref = self.db.collection('messages')
        query = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING)

        def on_snapshot(doc_snapshot, changes, read_time):
            for change in changes:
                if change.type.name == 'ADDED':
                    latest_message = change.document.to_dict()
                    alias = latest_message['alias']
                    message_text = latest_message['text']

                    self.new_message_event.set()

        query.on_snapshot(on_snapshot)

    def read_message(self):
        while True:
            self.new_message_event.wait()

            messages_ref = self.db.collection('messages')
            query = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1)
            latest_message = query.get()[0].to_dict()
            alias = latest_message['alias']
            message_text = latest_message['text']

            self.new_message_event.clear()
            return alias, message_text

    def write_message(self, alias, message_text):
        messages_ref = self.db.collection('messages')
        messages_ref.add({
            'alias': alias + '#BOT',
            'text': message_text,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
