import api.models as api_models
import authentication.models as auth_models
from authentication._serializers.passenger_serializers import PassengerSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreatePassengerNotificationSerializer(ModelSerializer):
    passenger = serializers.UUIDField(required=True, write_only=True)
    expo_token = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.PassengerNotification
        fields = ['expo_token', 'passenger']
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
        expo_token = validated_data.pop('expo_token', None)
        passenger = validated_data.pop('passenger', None)

        if not passenger:
            raise ValidationError({'detail': 'This field is required!'})
        if not expo_token:
            raise ValidationError({'detail': 'This field is required!'})

        passenger_instances = auth_models.Passenger.objects.all().filter(id=passenger)
        notification_instances = api_models.Notification.objects.all().filter(
            expo_token=expo_token)

        if not passenger_instances.exists():
            raise ValidationError({'detail': 'This field is required!'})

        if not notification_instances.exists():
            notification_instance = api_models.Notification.objects.create(
                expo_token=expo_token)
        else:
            notification_instance = notification_instances[0]

        passenger_notification_instance = api_models.PassengerNotification.objects.create(passenger=passenger_instances[0], notification=notification_instance
                                                                                    )
        return passenger_notification_instance


class PassengerNotificationSerializer(ModelSerializer):
    class Meta:
        model = api_models.PassengerNotification
        fields = ['id', 'passenger', 'notification', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
