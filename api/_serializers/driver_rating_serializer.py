from api._serializers.rating_serializer import RatingSerializer
import api.models as api_models
import authentication.models as auth_models
from core.modules.rest_framework_modules import serializers
from authentication._serializers.driver_serializers import DriverSerializer
from core.modules.rest_framework_modules import serializers
from core.utilities.rest_exceptions import (ValidationError)
from core.mixins.serializer_mixins import ModelSerializer


class CreateDriverRatingSerializer(ModelSerializer):
    driver = serializers.UUIDField(required=True, write_only=True)
    rate_value = serializers.FloatField(required=True, write_only=True)
    reason = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = api_models.DriverRating
        fields = ['rate_value', 'reason', 'driver']
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

        rate_instance = api_models.Rating.objects.create(**validated_data)

        driver_rating_instance = api_models.DriverRating.objects.create(
            rating=rate_instance, driver=driver_instances[0])
        return driver_rating_instance


class DriverRatingSerializer(ModelSerializer):
    rating = RatingSerializer()
    driver = DriverSerializer()

    class Meta:
        model = api_models.DriverRating
        fields = ['id', 'rating', 'driver']
        lookup_field = 'id'
        depth = 1

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
