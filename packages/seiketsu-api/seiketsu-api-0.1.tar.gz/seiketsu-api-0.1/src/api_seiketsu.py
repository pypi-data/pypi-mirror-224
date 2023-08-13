import firebase_admin
from firebase_admin import credentials, firestore, auth
from typing import List, Tuple
from google.oauth2 import service_account

firebase_project_id = 'animomik-20f94'  # Replace with your Firebase project ID

# Replace placeholders with their actual values from your service account JSON file
credentials_dict = {
  "type": "service_account",
  "project_id": "animomik-20f94",
  "private_key_id": "175d516c58e184472168501509fdd2fefb87e10e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCpNKtTivZxxs9J\nTZP6AIcE8uSoR9cS9oFIBMBsFsyO8layeda8MmIyrz7C3tYZYJMdSVpMZf2OudoZ\nw8YVZC0QDHxtHRmIMSZYaNEFhiDnIgYAD3N4wchppFB+k8bt8dhBg2OpQXJLAbry\nuJYFbUG/eF+5RrX1wekVhpuioTOtvywE/iLv/62Vr0N/+eBadsh7YwclL1+3kGjD\nuQ1Gu0RYCcLMmr4oT6RhqHV/Jr4qDAxZIJZncU00l/Q19gTogJP7RvtsTt+iJ/9W\noExhgb9C6d2Dw7GOpGAoRRyKbRYRdQ8fx0mXyjOmtnDSOj86fQP+65vP9c2WekQU\ndp+tRTnzAgMBAAECggEALfjfa61f0/3eJ95qDAzEonWT5pzONJrA+V5BIZz4KwZw\nw8EStMNDpt2yQaPlq7NvhQ9+9y7muzaHqWRllz5GeAvMaqDzZOtlrbOcxtFwcxvt\nYWrRRsfvubQpIprn+5Iv3WzjUQM1GGf58SRxrjvHF0yPRXmOypzKxUxzULZXoibT\nRWZRjSCd7lAz/J8G3WPrOMGwoz5NMzHUMBXFSQxVXnY8BdbeRN0lhq4J/kPXv633\nVSiUB/zZsUf/OVdIW4bOHVC3WtAO60h7XWiZZf76x71yz53CCZvlzlzkkukxALnY\nQoJE6moL+gDVYKtyGh5opOFjd1IWzdVtotzE9tNp4QKBgQDiFNrZ46QeYTb0Ei37\npthtUEA5CJyo4I9KXIb4IQE1hcZtcOMioo0+eO1gyOzb+Tbo1Egn0N49FU27mXWB\nTFk5s1ErXwcMXP1SACEo4D0Jblov/4I47CLqqiWvV57IdD4UySuai2IVoL9ZT3gu\nPQOiZ1PtUozCon6yyUXYfpO6+wKBgQC/mP1CJ7q4mQz+pWSOv7aAQHzB6AaAakT1\ni16EYt0wkUisvd8sBFgshJXrrMwKrwoeU7Sdn0Y8ZuvmTBGc5vSxUZwW6My7U8hT\n8TIQv6GTX0w2UIS7jiYHTV/D7KYMXyaS4ASAbYZrMwL57f/9/WFq+e6SgG+Y1AEn\nTQ3B+9JLaQKBgBQ+IcpYo51EvxLjfdKGgeJnyRhSORS15p6V4k/dRKpyK+4oqW20\neEkbssVzuCGKEuyN9Vf7T6rQeYFOoELPfz23XJExlQP6X4Q0FsP+L/jkNJcPna1T\nF11DltQ4WDNClTxvNsRDrqiZGAj7IJujQuwLrGwXdBsJSabgdqyHyNp5AoGADDPk\nPWhmXgdxam6CPw06xGRXDcqHT3p1NeZQeMILMGKwbEATjKwiKYOwQLharnuDe3b9\nU+SnBoXPlHVX0dRr1TdLZ7IgB/ZIFgCQnbx2v/ob0oHCUme1SFXHOaVC1hrhTA10\ne/F91CoFkIF2Amk24SdV6ILBmMw33pbrv2UYebECgYBXgq2CQftU7nPvnhQ4ynNy\n1nsowyYmyTsBvcwRNNIO0Udp7vYS6/M+B+gzPtMFWdZ7LMoARoNASaPSwcndHq1m\nJlxvxeFJ7VKIN4yUcNRigYVUmepcYNmloNRF4vCvIEnulqnZQU7riJ6Kv6tK9US4\ngaUuQLx5jRgc6nprQnGbKg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-qdx53@animomik-20f94.iam.gserviceaccount.com",
  "client_id": "100211968033591147464",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qdx53%40animomik-20f94.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Create a ServiceAccountCredentials object from the credentials dictionary
credentials = service_account.Credentials.from_service_account_info(credentials_dict)

# Initialize Firebase Admin SDK with the credentials object
firebase_admin.initialize_app(credentials, {'projectId': firebase_project_id})

# Get a reference to the Firestore database
db = firestore.client()

class SeiketsuAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._validate_api_key()

        if not firebase_admin._apps:
            cred = credentials.Certificate(db)
            firebase_admin.initialize_app(cred, {'projectId': firebase_project_id})
        self.firestore_db = firestore.client()

    def _validate_api_key(self):
        # Validate the API key, raise a ValueError if it's not valid
        if self.api_key != 'your_issued_api_key':  # Replace 'your_issued_api_key' with a valid key
            raise ValueError('Invalid API key provided')

    def get_messages(self) -> List[Tuple[str, str]]:
        messages_ref = self.firestore_db.collection('messages')
        messages_docs = messages_ref.order_by('timestamp').stream()
        messages = [(doc.get('alias'), doc.get('text')) for doc in messages_docs]
        return messages

    def send_message(self, nickname: str, text: str) -> None:
        message_ref = self.firestore_db.collection('messages')
        message_ref.add({
            'alias': nickname,
            'text': text,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
