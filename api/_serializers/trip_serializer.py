import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from api._serializers.vehicle_serializer import VehicleSerializer
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateTripSerializer(ModelSerializer):
    driver = serializers.UUIDField()

    class Meta:
        model = api_models.Trip
        fields = ['id','driver', 'pick_up_location',
                  'destination', 'date', 'reason']
        lookup_field = 'id'
        depth = 2
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        _request = self.context['request']
        request = {'request': _request, 'validated_data': validated_data}
        driver = validated_data.pop('driver', None)

        if not driver:
            raise ValidationError({'driver': 'This field is required!'})

        driver_instances = auth_models.Driver.objects.all().filter(id=driver)


        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})

        # trip_instances = api_models.Trip.objects.all().filter(
        #     driver=driver_instances[0]
        # ).filter(
        #     vehicle=vehicle_instances[0]
        # )

        # if trip_instances.exists():
        #     raise ValidationError({
        #         'data': {
        #             'code': 400,
        #             'error': 'Bad Request',
        #             'message': 'The specified Trip has already requested!'}})

        trip_instance = api_models.Trip.objects.create(
            driver=driver_instances[0],
            **validated_data
        )
        return trip_instance


class TripSerializer(ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = api_models.Trip
        fields = ['id', 'driver', 'pick_up_location',
                  'destination', 'date', 'reason', 'status', 'started_at','vehicle', 'ended_at','cost']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
