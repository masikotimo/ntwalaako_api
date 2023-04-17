from core.management.retrieval import Retriever
from authentication.models import Passenger


class PassengerRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Passenger.objects.get(id=instance_id)
        return instance
