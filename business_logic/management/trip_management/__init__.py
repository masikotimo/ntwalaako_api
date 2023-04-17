from core.management import AbstractManager

from .creation import TripCreator as Creator
from .list_viewing import TripListViewer as ListViewer
from .retrieval import TripRetriever as Retriever
from .updating import TripUpdater as Updater
from .patching import TripPatcher as Patcher
from .deletion import TripDeleter as Deleter


class TripManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
