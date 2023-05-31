from typing import List
from django.core.mail import EmailMessage
import threading
from sendgrid import sendgrid
from rest_framework.response import Response
from django.conf import settings


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class EmailSender:
    @staticmethod
    def send_email(data) -> Response:
        sender = "masikotimo@gmail.com"
        subject= data['email_subject']
        message = data['email_body']
        to=[data['to_email']]

        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        params = {
            "personalizations": [{"to": [{"email": k} for k in to], "subject": subject}],
            "from": {"email": sender},
            "content": [{"type": "text/html", "value": message}],
        }
        return sg.client.mail.send.post(request_body=params)

