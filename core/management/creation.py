from abc import ABC, abstractmethod

class Creator(ABC):
    """
        Creation Interface

    """    

    @abstractmethod
    def create(self, validated_data:dict) -> object :
        pass
