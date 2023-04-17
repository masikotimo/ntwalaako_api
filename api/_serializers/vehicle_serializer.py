import api.models as api_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from core.mixins.serializer_mixins import ModelSerializer


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = api_models.Vehicle
        exclude = ["created_by", "lastupdated_by", "created_at",
                   "lastupdated_at", ]
        lookup_field = 'id'
        depth = 0

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
