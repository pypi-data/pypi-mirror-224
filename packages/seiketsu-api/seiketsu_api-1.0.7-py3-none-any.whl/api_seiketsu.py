import os
import json
from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()
credentials_json = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"])
credentials = service_account.Credentials.from_service_account_info(credentials_json)
db = firestore.Client(credentials=credentials)


def read_last_message():
    messages_ref = db.collection('messages')
    last_message = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).get()

    if last_message:
        message = last_message[0].to_dict()
        return message
    else:
        return None


def write_message(alias, text):
    messages_ref = db.collection('messages')
    message_data = {
        'alias': alias,
        'text': text,
        'timestamp': firestore.SERVER_TIMESTAMP
    }
    messages_ref.add(message_data)
