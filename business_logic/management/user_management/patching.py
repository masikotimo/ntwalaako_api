from core.management.patching import Patcher
from authentication.models import User

class UserPatcher(Patcher):
    
    def  patch(self, instance, validated_data: dict) -> object:
        for [key, value] in validated_data:
            instance[key] = instance[value]
        return instance.save()
