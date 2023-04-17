from rest_framework import serializers
from authentication.models import *
from api.models import *
from core.utilities.rest_exceptions import (ValidationError)


class DriverAvailableSerializer(serializers.Serializer):
    driver = serializers.UUIDField(required=True, write_only=True)
