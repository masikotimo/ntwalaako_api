from core.management.list_viewing import ListViewer
from api.models import Trip


class TripListViewer(ListViewer):

    def get_list(self) -> list:
        return Trip.objects.all()
