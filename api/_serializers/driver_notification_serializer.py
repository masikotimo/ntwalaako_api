import api.models as api_models
import authentication.models as auth_models
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDriverNotificationSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    expo_token = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.DriverNotification
        fields = ['expo_token', 'driver']
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
        driver = validated_data.pop('driver', None)

        if not driver:
            raise ValidationError({'driver': 'This field is required!'})
        if not expo_token:
            raise ValidationError({'expo_token': 'This field is required!'})

        driver_instances = auth_models.Driver.objects.all().filter(id=driver)
        notification_instances = api_models.Notification.objects.all().filter(
            expo_token=expo_token)

        if not driver_instances.exists():
            raise ValidationError({'driver': 'Invalid value!'})

        if not notification_instances.exists():
            notification_instance = api_models.Notification.objects.create(
                expo_token=expo_token)
        else:
            notification_instance = notification_instances[0]

        driver_notification_instance = api_models.DriverNotification.objects.create(driver=driver_instances[0], notification=notification_instance
                                                                                    )
        return driver_notification_instance


class DriverNotificationSerializer(ModelSerializer):
    class Meta:
        model = api_models.DriverNotification
        fields = ['id', 'driver', 'notification', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
