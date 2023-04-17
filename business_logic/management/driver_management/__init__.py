from core.management import AbstractManager

from .creation import DriverCreator as Creator
from .list_viewing import DriverListViewer as ListViewer
from .retrieval import DriverRetriever as Retriever
from .updating import DriverUpdater as Updater
from .patching import DriverPatcher as Patcher
from .deletion import DriverDeleter as Deleter


class DriverManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
