import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateBlacklistSerializer(ModelSerializer):

    class Meta:
        model = api_models.Blacklist
        fields = ['reason']
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

        blacklist_instance = api_models.Blacklist.objects.create(
            **validated_data)
        return blacklist_instance


class BlacklistSerializer(ModelSerializer):
    class Meta:
        model = api_models.Blacklist
        fields = ['id', 'reason', ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
