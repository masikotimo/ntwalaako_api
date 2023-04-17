from abc import ABC, abstractmethod

class Patcher(ABC):
    """
        Patch Interface

    """    

    @abstractmethod
    def patch(self, instance, validated_data:dict) -> object :
        pass
