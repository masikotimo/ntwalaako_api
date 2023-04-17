from core.management.retrieval import Retriever
from authentication.models import Driver


class DriverRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Driver.objects.get(id=instance_id)
        return instance
