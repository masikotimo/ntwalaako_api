"""
    Courier Account Managers
"""
from rest_framework.response import Response
from rest_framework import status
from api.models import Vehicle

from business_logic.management.driver_management import DriverManager
from business_logic.management.user_management import UserManager
from authentication._serializers import user_serializers
from business_logic.utilities.mailing import EmailVerificationLinkSender
from core.utilities.auth import get_authenticated_user
from core.utilities.rest_exceptions import (ValidationError)

RegisterUserSerializer = user_serializers.RegisterUserSerializer


class AccountCreator():

    def create(self, request):
        """
        A method for registering a carbooking Courier member
        """
        try:
            validated_data = request['validated_data']
            request = request['request']
            email = validated_data.get('email')
            vehicle = validated_data.pop('vehicle', None)
            if not vehicle:
                    raise ValidationError({'detail': 'vehicle field is required!'})

            vehicle_instances = Vehicle.objects.all().filter(id=vehicle)

            if not vehicle_instances.exists():
                raise ValidationError({'detail': 'Vehicle Does not exist!'})

            user_count = UserManager().get_list().filter(email=email).count() or 0
            if user_count < 1:
                user = RegisterUserSerializer().create(validated_data)
            user = UserManager().get_list().filter(email=email)[0]
            driver_count = DriverManager().get_list().filter(user=user).count() or 0

            if driver_count > 0:
                response_data = {
                    'email': [
                        'Courier with this email address (' +
                        email + ') already exists.'
                    ]
                }
                return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.is_driver = True
                user.save()
                validated_data = {'user': user,'vehicle':vehicle_instances[0]}
                driver = DriverManager().create(validated_data)
                authenticated_user = get_authenticated_user(
                    request)  # or AnonymousUser
                if authenticated_user.__str__() == 'AnonymousUser':
                    authenticated_user = user
                driver.registered_by = authenticated_user
                driver.lastupdated_by = authenticated_user
                driver.save()
                return EmailVerificationLinkSender(request).send()
        except Exception as exception:
            raise exception
