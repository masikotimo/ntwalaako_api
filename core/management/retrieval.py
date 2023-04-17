from abc import ABC, abstractmethod

class Retriever(ABC):
    """
        Retrieval Interface

    """    

    @abstractmethod
    def retrieve(self, instance_id) -> object :
        pass
