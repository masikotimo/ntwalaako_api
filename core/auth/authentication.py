"""
    Check login credentials to see if you recognize a user trying to login
"""

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from abc import ABC as AbstractClass, abstractmethod

class AbstractAuthentication(AbstractClass):
    _user = None

    def set_user(self, user):
        self._user = user

    def get_user(self):
        return self._user

    @abstractmethod
    def is_authenticated(self):
        pass

class EmailAndPasswordAuthentication(AbstractAuthentication):

    def _is_authenticated(self, login_data):
        email = login_data.get('email', '')
        password = login_data.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials, Please Try again')
        if not user.is_active:
            raise AuthenticationFailed(
                'Your Account is Disabled. Contact Administrator')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified!')
        self.set_user(user)
        return True

    def is_authenticated(self, login_data):
        return self._is_authenticated(login_data)

