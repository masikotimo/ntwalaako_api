from core.management.retrieval import Retriever
from authentication.models import User


class UserRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = User.objects.get(id=instance_id)
        return instance
