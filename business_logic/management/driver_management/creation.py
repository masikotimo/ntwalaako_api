from core.management.creation import Creator
from authentication.models import Driver


class DriverCreator(Creator):

    def create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        client = Driver.objects.create(user=user)
        return client
