import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateNotificationSerializer(ModelSerializer):

    class Meta:
        model = api_models.Notification
        fields = ['expo_token']
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

        if not expo_token:
            raise ValidationError({'expo_token': 'This field is required!'})

        notification_instance = api_models.Notification.objects.create(expo_token=expo_token
                                                                       )
        return notification_instance


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = api_models.Notification
        fields = ['id', 'expo_token', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
