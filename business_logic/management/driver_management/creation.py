from core.management.creation import Creator
from authentication.models import Driver


class DriverCreator(Creator):

    def create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        vehicle = validated_data.get('vehicle')
        client = Driver.objects.create(user=user,vehicle=vehicle)
        return client
