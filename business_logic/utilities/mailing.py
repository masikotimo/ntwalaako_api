from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from core.utilities.mailing import EmailSender
from business_logic.management.user_management import UserManager


class EmailVerificationLinkSender:

    def __init__(self, request):
        self.request = request
        self.email = request.data['email']

    def _send(self):

        user = UserManager().get_list().filter(email=self.email)[0]
        email = user.email
        token = RefreshToken.for_user(user)
        current_site = get_current_site(self.request).domain
        relative_link = reverse('verify-email')
        absurl = current_site+relative_link+'?token='+str(token)
        # absurl = 'https://www.api.carbooking.ug'+relative_link+'?token='+str(token)
        email_body = 'Hi '+email+' You are almost there.\n\
        Please follow the link below to verify your email and activate your carbooking account.\n' \
                 + absurl
        data = {
            'email_subject': 'Email Verification and Account Activation',
            'to_email': email,
            'email_body': email_body
        }
        EmailSender.send_email(data)

        response_data = {
            'email': email,
            'registration_status': 'success',
            'message': 'Email verification link has been sent to this email (' + email + ')'
        }
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def send(self):
        return self._send()
