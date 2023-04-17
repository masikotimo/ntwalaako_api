from core.management.deletion import Deleter
from api.models import Trip


class TripDeleter(Deleter):

    def delete(self, instance_id):
        return Trip.objects.delete(id=instance_id)
