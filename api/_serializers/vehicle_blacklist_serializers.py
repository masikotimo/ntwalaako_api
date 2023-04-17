import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateVehicleBlacklistSerializer(ModelSerializer):
    vehicle = serializers.UUIDField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.VehicleBlacklist
        fields = ['reason', 'vehicle']
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
        vehicle = validated_data.pop('vehicle', None)
        vehicle_instances = api_models.Vehicle.objects.all().filter(id=vehicle)

        if not vehicle_instances.exists():
            raise ValidationError({'vehicle': 'Invalid value!'})

        vehicle_instance = vehicle_instances[0]
        vehicle_instance.is_available = False
        vehicle_instance.save()

        blacklist_instance = api_models.Blacklist.objects.create(
            **validated_data)

        vehicle_blacklist_instance = api_models.VehicleBlacklist.objects.create(
            vehicle=vehicle_instance, blacklist=blacklist_instance)

        return vehicle_blacklist_instance


class VehicleBlacklistSerializer(ModelSerializer):
    class Meta:
        model = api_models.VehicleBlacklist
        fields = ['id', 'blacklist', 'vehicle']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
