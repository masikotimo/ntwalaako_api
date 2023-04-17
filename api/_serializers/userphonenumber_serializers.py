from api.models import UserPhoneNumber
from api._serializers.phonenumber_serializers import PhoneNumberSerializer
from core.mixins.serializer_mixins import ModelSerializer


class UserPhoneNumberSerializer(ModelSerializer):
    phone_number = PhoneNumberSerializer()

    class Meta:
        model = UserPhoneNumber
        fields = ['id', 'phone_number', 'primary']
        lookup_field = 'id'
        depth = 1
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
