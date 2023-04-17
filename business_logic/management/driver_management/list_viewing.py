from core.management.list_viewing import ListViewer
from authentication.models import Driver


class DriverListViewer(ListViewer):

    def get_list(self):
        return Driver.objects.all()
