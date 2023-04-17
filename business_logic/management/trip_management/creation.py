from core.management.creation import Creator
from api.models import Trip


class TripCreator(Creator):

    def create(self, validated_data: dict) -> object:
        return Trip.objects.create(validated_data)
