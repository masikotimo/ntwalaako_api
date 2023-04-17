from . import _user
from business_logic.auth.authentication import DriverEmailAndPasswordAuthentication
from business_logic.auth import AuthController
User = _user.User


class Driver(User):
    """
    A controller for Driver as a system user.
    """

    def __init__(self,):
        super()

    # Mutators

    # Accessors

    # Generic User Operations
    def login(self, login_data):
        self.set_auth_controller(AuthController())
        self.get_auth_controller().set_in_logger(
            DriverEmailAndPasswordAuthentication())
        InLogger = self.get_auth_controller().get_in_logger()
        return InLogger.login(login_data)
