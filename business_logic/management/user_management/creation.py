from core.management.creation import Creator
from authentication.models import User

class UserCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        user = User.objects.create(validated_data)
        return user
