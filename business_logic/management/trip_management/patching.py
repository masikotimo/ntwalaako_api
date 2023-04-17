from core.management.patching import Patcher
from api.models import Trip


class TripPatcher(Patcher):

    def patch(self, instance, validated_data: dict) -> object:
        for [key, value] in validated_data:
            instance[key] = instance[value]
        return instance.save(commit=True)
