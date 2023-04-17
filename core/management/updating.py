from abc import ABC, abstractmethod

class Updater(ABC):
    """
        Update Interface

    """    

    @abstractmethod
    def update(self, instance, validated_data:dict) -> object :
        pass
