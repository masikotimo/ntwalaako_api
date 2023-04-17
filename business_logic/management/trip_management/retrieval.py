from core.management.retrieval import Retriever
from api.models import Trip


class TripRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Trip.objects.get(id=instance_id)
        return instance
