import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

API_KEY = os.getenv('FIREBASE_API_KEY')


def send_desktop_message(token):

    url = 'https://fcm.googleapis.com/fcm/send'

    data = {
        "notification": {
            "title": "Pending Request",
            "body": "A new Trip request has been issued."
        },

        'registration_ids': [token]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+API_KEY
    }

    try:

        res = requests.post(url, data=json.dumps(data), headers=headers)
        return res.json()
    except Exception as exception:
        raise exception


# print(send_desktop_message())
