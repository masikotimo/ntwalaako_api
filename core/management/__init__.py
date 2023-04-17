from abc import ABC, abstractmethod,abstractproperty
from django.db import models
from .management import Managenent
from .creation import Creator
from .list_viewing import ListViewer
from .retrieval import Retriever
from .updating import Updater
from .patching import Patcher
from .deletion import Deleter

class Model(models.Model):
    pass

class AbstractManager(Managenent, ABC):

    # # Properties : Encapsulation
    # @property
    # @abstractmethod
    # def model(self):
    #     pass


    # Data Fields : Encapsulation : Information Hidding
    _creator:Creator
    _listViewer:ListViewer
    _retriever:Retriever
    _updater:Updater
    _patcher:Patcher
    _deleter:Deleter


    # Data Operators : Encapsulation
    def create(self, validated_data: dict) -> object:
        # Cohesion : Coupling : Delegation
        return self._creator.create(validated_data)

    def get_list(self):
        return self._listViewer.get_list()

    def retrieve(self, instance_id) -> object:
        return self._retriever.retrieve(instance_id)

    def update(self, instance: object, validated_data:dict) -> object :
        return self._updater.update(instance, validated_data)

    def patch(self, instance: object, validated_data:dict) -> object :
        return self._patcher.patch(instance, validated_data)

    def delete(self, instance_id) -> object :
        return self._deleter.delete(instance_id)


    # Setters : Data Mutators : The Mutator Pattern
    def set_creator(self, creator:Creator):
        self._creator = creator

    def set_list_viewer(self, listViewer:ListViewer):
        self._listViewer = listViewer

    def set_retriever(self, retriever:Retriever):
        self._retriever = retriever

    def set_updater(self, updater:Updater):
        self._updater = updater

    def set_patcher(self, patcher:Patcher):
        self._patcher = patcher

    def set_deleter(self, deleter:Deleter):
        self._deleter = deleter


    # Getters : Data Accessors : The Accessor Pattern
    def get_creator(self):
        return self._creator

    def get_list_viewer(self):
        return self._listViewer

    def get_retriever(self):
        return self._retriever

    def get_updater(self):
        return self._updater

    def get_patcher(self):
        return self._patcher

    def get_deleter(self):
        return self._deleter
