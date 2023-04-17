from core.management.deletion import Deleter
from authentication.models import Driver


class DriverDeleter(Deleter):

    def delete(self, instance_id):
        return Driver.objects.delete(id=instance_id)
