"""
    Check login credentials to see if you recognize a user trying to login
"""

from abc import ABC as AbstractClass
from business_logic.management.passenger_management import PassengerManager
from business_logic.management.driver_management import DriverManager

from core.auth.authentication import EmailAndPasswordAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone


class UserAuthentication(AbstractClass):
    _auth_type = None

    def set_auth_type(self, auth_type):
        self._auth_type = auth_type

    def get_auth_type(self):
        return self._auth_type

    def user_login(self, login_data):
        auth = self.get_auth_type()
        is_authenticated = auth.is_authenticated(login_data)
        if is_authenticated:
            user = auth.get_user()
            return user


class PassengerEmailAndPasswordAuthentication(UserAuthentication):

    def login(self, login_data):
        try:
            self.set_auth_type(EmailAndPasswordAuthentication())
            user = self.user_login(login_data)
            passenger_count = PassengerManager().get_list().filter(user=user).count() or 0
            if passenger_count < 1:
                raise AuthenticationFailed(
                    'Invalid Credentials, Possibly you are not registered as a Passenger Member.')
            passenger = PassengerManager().get_list().filter(user=user)[0]
            return_object = {
                'login_status': 'success',
                'email': user.email,
                'user_id': user.Id,
                'tokens': user.tokens()
            }
            return_object['passenger_id'] = passenger.id
            user.last_login = timezone.now()
            user.save()
            return return_object
        except Exception as exception:
            raise exception


class DriverEmailAndPasswordAuthentication(UserAuthentication):

    def login(self, login_data):
        try:
            self.set_auth_type(EmailAndPasswordAuthentication())
            user = self.user_login(login_data)
            driver_count = DriverManager().get_list().filter(user=user).count() or 0
            if driver_count < 1:
                raise AuthenticationFailed(
                    'Invalid Credentials, Possibly you have not yet signed up as a Vendor.')
            driver = DriverManager().get_list().filter(user=user)[0]
            return_object = {
                'login_status': 'success',
                'email': user.email,
                'user_id': user.Id,
                'tokens': user.tokens()
            }
            return_object['driver_id'] = driver.id
            user.last_login = timezone.now()
            user.save()
            return return_object
        except Exception as exception:
            raise exception
