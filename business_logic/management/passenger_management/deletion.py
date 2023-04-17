from core.management.deletion import Deleter
from authentication.models import Passenger


class PassengerDeleter(Deleter):

    def delete(self, instance_id):
        return Passenger.objects.delete(id=instance_id)
