from abc import ABC, abstractmethod

class Deleter(ABC):
    """
        Deletion Interface

    """    

    @abstractmethod
    def delete(self, instance_id):
        pass
