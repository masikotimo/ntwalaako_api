from abc import ABC as AbstractClass

from business_logic.user_accounts import UserAccountsController
from business_logic.auth import AuthController
from business_logic.auth.authentication import PassengerEmailAndPasswordAuthentication


class AbstractUser(AbstractClass):
    """
    A controller for the system user.
    """
    _accounts_controller: None
    _auth_controller = None

    # Mutators

    def set_accounts_controller(self, accounts_controller):
        self._accounts_controller = accounts_controller

    def set_auth_controller(self, auth_controller):
        self._auth_controller = auth_controller

    # Accessors

    def get_accounts_controller(self):
        return self._accounts_controller

    def get_auth_controller(self):
        return self._auth_controller


class User(AbstractUser):
    # Generic User Operations
    def register_user(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_user(request)

    def register_passenger(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_passenger(request)

    def register_driver(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_driver(request)

    def register_fleetmanager(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_fleetmanager(request)

    def register_systemadmin(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_systemadmin(request)

    def login(self, login_data):
        self.set_auth_controller(AuthController())
        return self.get_auth_controller().in_logger.login(login_data)
