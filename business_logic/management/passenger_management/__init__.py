from core.management import AbstractManager

from .creation import PassengerCreator as Creator
from .list_viewing import PassengerListViewer as ListViewer
from .retrieval import PassengerRetriever as Retriever
from .updating import PassengerUpdater as Updater
from .patching import PassengerPatcher as Patcher
from .deletion import PassengerDeleter as Deleter


class PassengerManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
