import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateRatingSerializer(ModelSerializer):

    class Meta:
        model = api_models.Rating
        fields = ['rate_value', 'reason']
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

        rating_instance = api_models.Rating.objects.create(
            **validated_data)
        return rating_instance


class RatingSerializer(ModelSerializer):
    class Meta:
        model = api_models.Rating
        fields = ['id', 'rate_value', 'reason']
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
