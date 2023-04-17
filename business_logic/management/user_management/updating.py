from core.management.updating import Updater
from authentication.models import User

class UserUpdater(Updater):
    
    def  update(self, instance, validated_data: dict) -> object:
        for [key, value] in validated_data:
            if(instance[key]):
                instance[key] = validated_data[value]
        return instance.save()

