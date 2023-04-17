from core.management.list_viewing import ListViewer
from authentication.models import Passenger


class PassengerListViewer(ListViewer):

    def get_list(self):
        return Passenger.objects.all()
