from abc import ABC, abstractmethod

class ListViewer(ABC):
    """
        Listing Interface

    """    

    @abstractmethod
    def get_list(self) -> list :
        pass
