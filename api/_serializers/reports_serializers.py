from rest_framework import serializers
from authentication.models import *
from api.models import *
from core.utilities.rest_exceptions import (ValidationError)


class ReportSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, write_only=True)
    organisation = serializers.UUIDField(required=True, write_only=True)
