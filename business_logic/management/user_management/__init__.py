from core.management import AbstractManager

from .creation import UserCreator as Creator
from .list_viewing import UserListViewer as ListViewer
from  .retrieval import UserRetriever as Retriever
from .updating import UserUpdater as Updater
from .patching import UserPatcher as Patcher
from .deletion import UserDeleter as Deleter

class UserManager(AbstractManager):
    
    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
