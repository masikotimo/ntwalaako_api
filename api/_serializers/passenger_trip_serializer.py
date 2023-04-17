import api.models as api_models
import authentication.models as auth_models
from authentication.serializers import DriverSerializer, PassengerSerializer
from api.serializers import TripSerializer
from authentication._serializers.passenger_serializers import PassengerSerializer
from core.mixins.serializer_mixins import ModelSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from django.utils import timezone


class CreatePassengerTripSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    pick_up_location = serializers.CharField(required=True, write_only=True)
    destination = serializers.CharField(required=True, write_only=True)
    date = serializers.DateTimeField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)
    vehicle = serializers.UUIDField(required=True, write_only=True)
    driver = serializers.UUIDField(required=True, write_only=True)

    data = serializers.DictField(
        required=False,
        read_only=True,
    )

    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'vehicle', 'driver', 'pick_up_location',
                  'destination', 'date',  'reason', 'passenger', 'data']

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        try:
            _request = self.context['request']
            request = {'request': _request, 'validated_data': validated_data}
            vehicle = validated_data.pop('vehicle', None)
            driver = validated_data.pop('driver', None)
            passenger = validated_data.pop('passenger', None)

            if not passenger:
                raise ValidationError({'passenger': 'This field is required!'})

            if not vehicle:
                raise ValidationError({'vehicle': 'This field is required!'})

            if not driver:
                raise ValidationError({'driver': 'This field is required!'})

            vehicle_instances = api_models.Vehicle.objects.all().filter(id=vehicle)
            driver_instances = auth_models.Driver.objects.all().filter(id=driver)
            passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)

            if not vehicle_instances.exists():
                raise ValidationError({'vehicle': 'Invalid value!'})

            if not driver_instances.exists():
                raise ValidationError({'driver': 'Invalid value!'})

            if not passenger_instances.exists():
                raise ValidationError({'passenger': 'Invalid value!'})

            trip_instance = api_models.Trip.objects.create(
                driver=driver_instances[0],
                vehicle=vehicle_instances[0],
                **validated_data
            )

            passenger_trip_instance = api_models.PassengerTrip.objects.create(
                passenger=passenger_instances[0],
                trip=trip_instance,
                # **validated_data
            )

            return passenger_trip_instance

        except Exception as exception:
            raise exception

        # return api_models.PassengerTrip.objects.create(trip=trip, passenger=passenger)


class PassengerTripSerializer(ModelSerializer):
    trip = TripSerializer(read_only=True)
    passenger = PassengerSerializer(read_only=True)

    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'trip', 'passenger']
        lookup_field = 'id'
        depth = 1


class UpdatePassengerTripSerializer(ModelSerializer):
    trip = serializers.UUIDField(required=True, write_only=True)
    pick_up_location = serializers.CharField(required=True, write_only=True)
    destination = serializers.CharField(required=True, write_only=True)
    status = serializers.CharField(required=False, write_only=True)
    date = serializers.DateTimeField(required=True, write_only=True)
    started_at = serializers.DateTimeField(
        required=False, write_only=True, allow_null=True)
    ended_at = serializers.DateTimeField(
        required=False, write_only=True, allow_null=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.PassengerTrip
        fields = ['id', 'reason', 'trip', 'pick_up_location', 'status',
                  'destination', 'date', 'started_at', 'ended_at']
        lookup_field = 'id'
        depth = 1

    def update(self, instance, validated_data):

        trip = validated_data.get('trip')

        trip_instances = api_models.Trip.objects.get(id=trip)
        if not trip_instances:
            raise ValidationError({'trip': 'Invalid value!'})

        trip_instances.reason = validated_data.get(
            'reason', instance.trip.reason)

        trip_instances.pick_up_location = validated_data.get(
            'pick_up_location', instance.trip.pick_up_location)

        trip_instances.destination = validated_data.get(
            'destination', instance.trip.destination)
        trip_instances.status = validated_data.get(
            'status', instance.trip.status)

        trip_instances.date = validated_data.get(
            'date', instance.trip.date)

        trip_instances.started_at = validated_data.get(
            'started_at')
        if trip_instances.started_at:
            trip_instances.vehicle.is_available = False
            trip_instances.driver.is_available = False
            trip_instances.driver.save()

        trip_instances.ended_at = validated_data.get(
            'ended_at', instance.trip.ended_at)

        if trip_instances.ended_at:
            trip_instances.vehicle.is_available = True
            trip_instances.driver.is_available = True
            trip_instances.driver.save()

        trip_instances.lastupdated_at = timezone.now()

        trip_instances.save()

        instance.save()
        return instance
