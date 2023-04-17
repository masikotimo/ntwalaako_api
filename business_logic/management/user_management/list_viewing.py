from core.management.list_viewing import ListViewer
from authentication.models import User

class UserListViewer(ListViewer):
    
    def get_list(self):
        return User.objects.all()
