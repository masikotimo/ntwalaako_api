from abc import ABC
from .creation import Creator
from .list_viewing import ListViewer
from .retrieval import Retriever
from .updating import Updater
from .patching import Patcher
from .deletion import Deleter


class Managenent(Creator, ListViewer, Retriever, Updater, Patcher, Deleter, ABC):
    pass
