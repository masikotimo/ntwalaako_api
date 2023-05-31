"""
Views for carbooking User Authentication (Account) Module
"""

import jwt

from authentication.models import PasswordResetInfo, User
from authentication.serializers import (
    PasswordResetConfirmSerializer, PasswordResetSerializer,
    SendVerificationLinkSerializer, UserLoginSerializer)
from core.utilities.mailing import EmailSender
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from car_booking_api import settings
from rest_framework import generics, status
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class SendVerificationLinkView(generics.GenericAPIView):
    serializer_class = SendVerificationLinkSerializer
    permission_classes = []

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        user_data = serializer.data
        user = User.objects.filter(email=user_data['email'])
        if not user.exists():
            return Response({'email': 'Invalid email!'}, status=status.HTTP_400_BAD_REQUEST)
        user = user[0]
        if user.is_verified:
            return Response({'email': 'Email already Verified!'}, status=status.HTTP_400_BAD_REQUEST)
        token = RefreshToken.for_user(user)
        current_site = get_current_site(request).domain
        relative_link = reverse('verify-email')
        absurl = 'http://'+current_site+relative_link+'?token='+str(token)
        # absurl = 'https://carbooking-api-3dx.herokuapp.com' + \
        #     relative_link+'?token='+str(token)

        email_body = 'Hi '+user.email+' You are almost done with your registration process with the carbooking Platform.\n\
        Please follow the link below to verify your email and activate your carbooking account.\n' \
                 + absurl
        data = {
            'email_subject': 'Email Verification and Account Activation',
            'to_email': user.email,
            'email_body': email_body
        }
        EmailSender.send_email(data)
        response_data = {
            'email': user_data['email'],
            'message': 'Email verification link has been sent to your email (' + user_data['email'] + ')'
        }
        return Response(data=response_data, status=status.HTTP_200_OK)


class VerifyEmailView(generics.GenericAPIView):
    serializer_class = SendVerificationLinkSerializer
    permission_classes = []
    renderer_classes = [StaticHTMLRenderer]

    # @renderer_classes([StaticHTMLRenderer])
    def get(self, request):
        try:
            token = request.GET.get('token')
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(Id=payload['Id'])
            # allauth_user = EmailAddress.objects.filter(user=user, email=user.email)
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response('<html><body><h1 style="color:green;">Successfully Registered!</h1></body></html>', content_type='text/html')

        except jwt.ExpiredSignatureError:
            # Technical Debt
            # return Response({'error':'Activation Link Expired!'}, status=status.HTTP_400_BAD_REQUEST)
            return Response('<html><body><h2 style="color:red;">Error: Activation link expired!</h2></body></html>', content_type='text/html')
        except jwt.exceptions.DecodeError:
            # Technical Debt
            # return Response({'error':'Invalid Token!'}, status=status.HTTP_400_BAD_REQUEST)
            return Response('<html><body><h2 style="color:red;">Error: Invalid token!</h2></body></html>', content_type='text/html')


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            data = serializer.validated_data
            # print(data)
            return Response(data=data, status=status.HTTP_200_OK)


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = []

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        user_data = serializer.data
        user = User.objects.filter(email=user_data['email'])
        if not user.exists():
            return Response({'email': 'Invalid email!'}, status=status.HTTP_400_BAD_REQUEST)
        user = user[0]

        reset_instance = PasswordResetInfo.objects.filter(user=user)

        if reset_instance.exists():
            reset_instance = reset_instance[0]
            reset_instance.delete()

        # Paanding..................
        # 1. Storing code and expiry date in the database
        PasswordResetInfo.objects.create(user=user)
        reset_instance = PasswordResetInfo.objects.filter(user=user)
        if not reset_instance.exists():
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        code = reset_instance[0].reset_code

        # relative_link = reverse('rest_password_reset_confirm')
        email_body = 'Hi ' + \
            user_data['email']+', Use this Code to reset your Password. Code: ' + \
            code + ' \n This code expires in 24 Hours'
        data = {
            'email_subject': 'Password Reset Code',
            'to_email': user_data['email'],
            'email_body': email_body
        }
        EmailSender.send_email(data)
        response_data = {
            'email': user_data['email'],
            'message': 'Password-reset code has been sent to your email (' + user_data['email'] + ')'
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

    permission_classes = []


class PasswordResetConfirmView(generics.GenericAPIView):
    # Procedure
    # --------------------------
    # 1. Receive data
    # 2. Validate email address
    # 3. Validate code
    # 4. Validate password(s)
    # 5. Reset password
    # 6. Remove record from database
    # 7. Send response
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = []

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        email_body = 'Hi '+user['email'] + \
            ', Your Password has been reset successfully'
        data = {
            'email_subject': 'Password Reset Successfully',
            'to_email': user['email'],
            'email_body': email_body
        }
        EmailSender.send_email(data)
        response_data = {
            'email': user['email'],
            'message': 'Password has been reset successfully'
        }
        PasswordResetInfo.objects.filter(user=serializer.user)[0].delete()
        return Response(data=response_data, status=status.HTTP_200_OK)
