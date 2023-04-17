from core.management.creation import Creator
from authentication.models import Passenger


class PassengerCreator(Creator):

    def create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        passenger = Passenger.objects.create(user=user)
        return passenger
