from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class BaseSerializer(FriendlyErrorMessagesMixin, serializers.Serializer):
    pass

class ModelSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    pass
