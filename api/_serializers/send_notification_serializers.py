from rest_framework import serializers
from authentication.models import *
from api.models import *
from core.utilities.rest_exceptions import (ValidationError)


class SendNotification:
    def __init__(self, token):
        self.token = token


class SendNotificationSerializer(serializers.Serializer):
    passenger_trip = serializers.UUIDField(required=True, write_only=True)

    def create(self, validated_data):
        passenger_trip = validated_data.pop('passenger_trip')

        passenger_trip_instances = PassengerTrip.objects.all().filter(id=passenger_trip)
        if not passenger_trip_instances.exists():
            raise ValidationError(
                {'passenger_trip': 'Passenger doesnt exist !'})

        trip = passenger_trip_instances[0].trip
        passenger = passenger_trip_instances[0].passenger

        passenger_notification_instances = PassengerNotification.objects.filter(
            passenger=passenger.id)

        driver_notification_instances = DriverNotification.objects.filter(
            driver=trip.driver.id)

        if not passenger_notification_instances.exists():
            raise ValidationError(
                {'passenger': 'Passenger has not yet regisered his application to receive notifications !'})

        if not driver_notification_instances.exists():
            raise ValidationError(
                {'Driver': 'Driver has not yet regisered his application to receive notifications !'})

        notification_details = {
            'passenger_token': passenger_notification_instances[0].notification.expo_token,
            'driver_token': driver_notification_instances[0].notification.expo_token,
            'driver_name': trip.driver.user.username,
            'passenger_name': passenger.user.username,
            'destination': trip.destination
        }

        return notification_details
