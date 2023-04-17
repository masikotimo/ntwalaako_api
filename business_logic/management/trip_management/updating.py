from core.management.updating import Updater
from api.models import Trip


class TripUpdater(Updater):

    def update(self, instance, validated_data: dict) -> object:
        for [key, value] in validated_data:
            if(instance[key]):
                instance[key] = validated_data[value]
        return instance.save(commit=True)
