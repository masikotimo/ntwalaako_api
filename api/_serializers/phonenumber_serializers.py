from api.models import PhoneNumber
from core.mixins.serializer_mixins import ModelSerializer


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'number']
        lookup_field = 'id'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
